import struct  # to format data for use in C networking library

# Use ID to match request and responses
# Create cute ID (1580) for demo
ICMP_ID = sum(ord(letter) for letter in "ACIT2515 Traceroute")


def checksum(data: bytes) -> int:
    """
    Calculate the checksum for ICMP packet.

    From RFC 972:
      The 16 bit one's complement of the one's complement sum of all 16
      bit words in the header.  For computing the checksum, the checksum
      field should be zero.  This checksum may be replaced in the
      future.

    Args:
        data: Byte data to calculate checksum for

    Returns:
        Checksum value

    References:
      RFC 792 Internet Control Message Protocol:
        https://datatracker.ietf.org/doc/html/rfc792

    """
    ALL_ONES_16_BITS = 0xFFFF
    checksum = 0

    # data arrives as bytes, determine if there are a even or odd number of two
    # byte groups
    odd_byte_count = len(data) % 2

    # loop over the data in two byte steps,
    for byte_pair_index in range(0, len(data) - odd_byte_count, 2):
        # shift byte to high order of byte of 16 bit chunk
        high_order_byte = data[byte_pair_index] << 8

        # get next byte for low order byte of 16 bit chunk
        low_order_byte = data[byte_pair_index + 1]

        # combine high and low order bytes into 16 bit chunk
        two_byte_chunk = high_order_byte + low_order_byte

        # Add chunk value to checksum_sum
        checksum += two_byte_chunk

    if odd_byte_count:
        # if number of bytes is odd the final byte pair has no low order byte
        # shift the remaining byte to the high order byte of the 16 bit chunk
        # effectively padding the low order byte with 0's
        checksum += data[-1] << 8

    # While checksum_sum  is larger than 0xFFFF
    # (i.e. there are bits above 16 bits to wrap around)
    while checksum >> 16:
        # Wrap checksum bits above maximum to low order bits and store them
        wrapped_bits_above_16 = checksum >> 16

        # remove bits above 16
        checksum_16_low_order_bits = checksum & ALL_ONES_16_BITS

        # add wrapped bits to checksum
        checksum = checksum_16_low_order_bits + wrapped_bits_above_16

    # mask with 0xFFFF to strictly limit to 16 bits
    ones_compliment = ~checksum & 0xFFFF

    return ones_compliment


def create_icmp_echo_request(packet_id: int = ICMP_ID, seq_num: int = 0) -> bytes:
    """
    Create an ICMP echo request packet.

    Args:
        packet_id: Packet identifier
        seq_num: Sequence number

    Returns:
        ICMP packet as bytes

    References:
        Python Structs:  https://docs.python.org/3/library/struct.html
        RFC 792 Internet Control Message Protocol:
            https://datatracker.ietf.org/doc/html/rfc792
        ICMP Echo Parameters:
            https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml

    """
    ICMP_ECHO_REQUEST = 8
    ICMP_ECHO_CODE = 0  # Echo Requests don't use the code set to zero
    ICMP_CHECKSUM_PLACEHOLDER = 0
    ICMP_DATA_PAYLOAD = b"PythonTraceroute"  # Data is unused, arbitrary

    # Format of data to "pack" into binary struct
    # '!' : network (big-endian) order, use standard sizes as specified
    # 'B' : python type: integer, c type: unsigned char, size: 1 byte
    # 'H' : python type: integer, c type: unsigned short, size: 2 bytes
    ICMP_FORMAT = "!BBHHH"

    # Creates a binary representation of the ICMP packet header.
    # with checksum 0, update checksum after building header
    header = struct.pack(
        ICMP_FORMAT,
        ICMP_ECHO_REQUEST,
        ICMP_ECHO_CODE,
        ICMP_CHECKSUM_PLACEHOLDER,
        packet_id,
        seq_num,
    )
    data = ICMP_DATA_PAYLOAD

    # Calculate actual checksum
    icmp_checksum = checksum(header + data)

    # Recreate header with correct checksum now that we know the actual packet values
    header = struct.pack(
        ICMP_FORMAT,
        ICMP_ECHO_REQUEST,
        ICMP_ECHO_CODE,
        icmp_checksum,
        packet_id,
        seq_num,
    )

    return header + data
