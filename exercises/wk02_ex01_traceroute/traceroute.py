"""
Traceroute implementation using recursion with actual TTL incrementing.
Demonstrates recursive problem solving by sending ICMP packets with increasing TTL values.

REQUIRES ADMINISTRATOR/ROOT PRIVILEGES to create raw sockets.
"""

import socket  # For low level networking
import time  # for measuring response time

from icmp_utility import create_icmp_echo_request


def recursive_traceroute(
    dest_ip, ttl: int = 1, max_hops: int = 30, timeout: float = 2.0
):
    """
    Recursively trace the route to a destination by incrementing TTL.

    Each recursive call sends an ICMP packet with an incremented TTL value.
    When a packet's TTL expires, the router sends back a "Time Exceeded" message,
    revealing that router's address. This continues until we reach the destination.

    Args:
        dest_ip: Destination IP address
        ttl: Current Time-To-Live value (increments with each recursive call)
        max_hops: Maximum number of hops to try
        timeout: Timeout in seconds for each probe

    Returns:
        None (prints results to console)

    """
    ICMP_ECHO_REPLY = 0
    ICMP_HEADER_LENGTH = 8
    ICMP_PORT = 0  # ICMP doesn't have ports so we set this to zero
    ICMP_TYPE_HEADER_POS = 0
    IP_ADDRESS_POS = 0
    IP_HEADER_LENGTH = 20
    MS_IN_SECOND = 1000
    RECEIVE_BUFFER_SIZE = 1024

    # Base case 1: exceeded maximum hops
    if ttl > max_hops:
        print(
            f"\nf{ttl} Reached maximum hops ({max_hops}) without reaching destination"
        )
        return

    try:
        # Create raw ICMP sockets for sending and receiving ECHO Requests
        send_socket = socket.socket(
            socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP
        )
        recv_socket = socket.socket(
            socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP
        )

        # Bind receive socket to capture ICMP responses
        # "": empty host captures on addresses
        recv_socket.bind(("", ICMP_PORT))

        # Set TTL for this hop - THIS IS THE KEY TO TRACEROUTE!
        # Each hop decrements TTL by 1, causing "Time Exceeded" at
        # routers when TTL reaches 0
        send_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

        # set timeout so that we don't wait forever to move to next hop
        recv_socket.settimeout(timeout)

        # re-use ttl as the ICMP request sequence number for tracking requests
        packet = create_icmp_echo_request(seq_num=ttl)

        send_time = time.time()
        send_socket.sendto(packet, (dest_ip, ICMP_PORT))

        # Try to receive response (socket timeout handles waiting)
        try:
            # wait to receive data
            data, addr_port = recv_socket.recvfrom(RECEIVE_BUFFER_SIZE)

            # Output will be in MS so convert elapsed time
            elapsed_time = (time.time() - send_time) * MS_IN_SECOND

            print(f"{ttl:02d} {addr_port[IP_ADDRESS_POS]:15s}  {elapsed_time:06.2f} ms")

            # Base case 2: reached destination
            # Extract ICMP Header from IP Datagram by slicing data bytes
            icmp_header = data[IP_HEADER_LENGTH : IP_HEADER_LENGTH + ICMP_HEADER_LENGTH]
            icmp_type = icmp_header[ICMP_TYPE_HEADER_POS]

            # Check if response is from the final destination address
            # or if it is a successful echo reply(ICMP type 0 = Echo Reply).
            # This indicates that the datagram got to the final destination
            if addr_port[IP_ADDRESS_POS] == dest_ip or icmp_type == ICMP_ECHO_REPLY:
                send_socket.close()
                recv_socket.close()
                return

        except socket.timeout:
            # Timeout - no response from this node, move on to next
            print(f"{ttl:02d} {' * TIMED_OUT * ':15}  {timeout:>06.2f} ms")

        send_socket.close()
        recv_socket.close()

        # Recursive case: increment TTL and continue to next hop
        time.sleep(0.1)  # Small delay between probes
        recursive_traceroute(dest_ip, ttl + 1, max_hops, timeout)

    except Exception as e:
        print(f"Error at hop {ttl}: {e}")
        return


def main():
    """Main function to run traceroute."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Traceroute implementation using recursion with ICMP packets.",
        epilog=str(
            "NOTE: This program requires Administrator/root privileges! \n"
            "On Windows: Run PowerShell/CMD as Administrator\n"
            "On Linux/Mac: Use sudo\n\n"
            "This implementation uses:\n"
            "  - Raw ICMP sockets (socket.IPPROTO_ICMP)\n"
            "  - ICMP Echo Request packets (Type 8)\n"
            "  - TTL incrementing for hop discovery\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "destination",
        help="Hostname or IP address to trace route to",
    )

    parser.add_argument(
        "-m",
        "--max-hops",
        type=int,
        default=10,
        help="Maximum number of hops (default: 10)",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=2.0,
        help="Timeout in seconds for each probe (default: 2.0)",
    )

    args = parser.parse_args()

    # Resolve hostname to IP address before starting traceroute
    try:
        dest_ip = socket.gethostbyname(args.destination)
        print(f"Tracing route to {args.destination} ({dest_ip})")
        print(f"Maximum hops: {args.max_hops}\n")
    except socket.gaierror:
        print(f"Error: Cannot resolve hostname '{args.destination}'")
        parser.exit(1)

    recursive_traceroute(dest_ip, max_hops=args.max_hops, timeout=args.timeout)


if __name__ == "__main__":
    main()
