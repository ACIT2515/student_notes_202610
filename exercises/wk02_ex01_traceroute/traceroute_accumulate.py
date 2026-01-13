"""
Traceroute implementation using recursion with actual TTL incrementing.
Demonstrates recursive problem solving by sending ICMP packets with increasing TTL values.

REQUIRES ADMINISTRATOR/ROOT PRIVILEGES to create raw sockets.
"""

import socket  # For low level networking
import time  # for measuring response time

from icmp_utility import create_icmp_echo_request


def recursive_traceroute(
    dest_ip,
    ttl: int = 1,
    max_hops: int = 30,
    timeout: float = 2.0,
    hops: list[dict] | None = None,
) -> list[dict[str, str]]:
    """
    Recursively trace the route to a destination by incrementing TTL.

    Each recursive call sends an ICMP packet with an incremented TTL value.
    When a packet's TTL expires, the router sends back a "Time Exceeded" message,
    revealing that router's address. This continues until we reach the destination.

    This function builds a list of hops (recursion accumulator) which is returned
    to the caller for printing, rather than printing side-effects during execution.

    Args:
        dest_ip: Destination IP address
        ttl: Current Time-To-Live value (increments with each recursive call)
        max_hops: Maximum number of hops to try
        timeout: Timeout in seconds for each probe
        hops: Accumulator list used to store hop data across recursive calls

    Returns:
        list[dict]: A list of dictionaries containing {"Node": ip, "Time": ms}
        for each hop

    """
    pass


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

    hops = recursive_traceroute(dest_ip, max_hops=args.max_hops, timeout=args.timeout)

    for hop in range(0, len(hops)):
        ttl = hop + 1
        print(f"{ttl:02d} {hops[hop]["Node"]:15}  {hops[hop]["Time"]:>7} ms")

    print()


if __name__ == "__main__":
    main()
