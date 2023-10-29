# Title: Project 4 - Validating a TCP Packet
# Name: Bennett Hamilton
# Date: 10/29/23
# Description: code that validates a TCP packet, making sure it hasn’t been corrupted in transit
# Reference: https://beej.us/guide/bgnet0/html/split/project-validating-a-tcp-packet.html

# function that calulates checksum from the psuedo header and data, returns the checksum
# ref: 16.7 Actually Computing the Checksum from "Reference" (see header)
def calculate_checksum(pseudo_header, tcp_data):
    # concatenate the pseudo header and the TCP data with zero checksum
    data = pseudo_header + tcp_data
    total = 0

    # compute the checksum of that concatenation
    for offset in range(0, len(data), 2):
        word = int.from_bytes(data[offset:offset + 2], 'big')
        total += word
        total = (total & 0xffff) + (total >> 16)

    return (~total) & 0xffff

# function that converts the dots-and-numbers IP addresses into bytestrings
# ref: https://www.geeksforgeeks.org/python-map-function/
# ref: https://stackoverflow.com/questions/21017698/why-does-bytesn-create-a-length-n-byte-string-instead-of-converting-n-to-a-b
def ip_to_bytes(ip):
    ip_parts = map(int, ip.split('.'))
    return bytes(ip_parts)      # using bytes() instead of .to_bytes since its an iterable

# function that validates the tcp packet data, return PASS or FAIL
# ref: https://www.w3schools.com/python/ref_file_readline.asp
def validate_tcp_packet(ip_filename, tcp_filename):
    # read the ip_addrs file
    with open(ip_filename, 'r') as ip_file:
        # split the line in two, the source and destination addresses
        source_ip, dest_ip = ip_file.readline().split(' ')
        # build psuedo header using source ip, destination ip, Zero = 0x00, PTLC = 0x06
        pseudo_header = ip_to_bytes(source_ip) + ip_to_bytes(dest_ip) + b'\x00\x06'

    # read the tcp_data file
    with open(tcp_filename, 'rb') as tcp_file:
        tcp_data = tcp_file.read()
        tcp_length = len(tcp_data)

        # convert the TCP length to a two-byte big-endian representation
        tcp_length_bytes = tcp_length.to_bytes(2, byteorder='big')

        pseudo_header += tcp_length_bytes

        if tcp_length % 2 == 1:     # build a new version of the TCP data that has the checksum set to zero
            tcp_data += b'\x00'

        checksum = calculate_checksum(pseudo_header, tcp_data)

        # extract the checksum from the original data in tcp_data file located "at byte offsets 16 and 17 inside the TCP header"
        # ref: 16.6 The TCP Header Checksum from "Reference" (see header)
        original_checksum = int.from_bytes(tcp_data[16:18], 'big')

        # compare the two checksums
        if checksum == original_checksum:
            print('PASS')
        else:
            print('FAIL')

# iterate through all files
for i in range(10):
    ip_filename = f'tcp_addrs_{i}.txt'
    tcp_filename = f'tcp_data_{i}.dat'
    print(f'Test {i+1}: ', end='')
    validate_tcp_packet(ip_filename, tcp_filename)