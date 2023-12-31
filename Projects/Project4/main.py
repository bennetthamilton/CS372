# Title: Project 4 - Validating a TCP Packet
# Name: Bennett Hamilton
# Date: 10/29/23
# Description: code that validates a TCP packet, making sure it hasn’t been corrupted in transit
# Reference: https://beej.us/guide/bgnet0/html/split/project-validating-a-tcp-packet.html

# function that calulates checksum from the psuedo header and data, returns the checksum
# ref: 16.7 Actually Computing the Checksum from "Reference" (see header)
def calculate_checksum(pseudo_header, tcp_data):

    tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]

    if len(tcp_zero_cksum) % 2 == 1:     # build a new version of the TCP data that has the checksum set to zero
        tcp_zero_cksum += b'\x00'

    # concatenate the pseudo header and the TCP data with zero checksum
    data = pseudo_header + tcp_zero_cksum
    total = 0

    # compute the checksum of that concatenation
    for offset in range(0, len(data), 2):
        word = int.from_bytes(data[offset:offset + 2], 'big')
        total += word
        total = (total & 0xffff) + (total >> 16)

    return (~total) & 0xffff

# function that converts the dots-and-numbers IP addresses into bytestrings
# ref: https://www.geeksforgeeks.org/python-map-function/
# ref: https://stackoverflow.com/questions/27001419/how-to-append-to-bytes-in-python-3
def ip_to_bytes(ip):
    ip_parts = ip.split('.')
    ip_bytes = b''
    # iterate through parts and covert to bytes
    for part in ip_parts:
        # convert each part (string) to an integer and then to a single byte
        part_int = int(part)
        part_byte = part_int.to_bytes(1, byteorder='big')
        ip_bytes += part_byte
    return ip_bytes

# function that validates the tcp packet data, return PASS or FAIL
# ref: https://www.w3schools.com/python/ref_file_readline.asp
def validate_tcp_packet(ip_filename, tcp_filename):
    # read the ip_addrs file
    with open(ip_filename, 'r') as ip_file:
        # split the line in two, the source and destination addresses
        source_ip, dest_ip = ip_file.readline().strip().split()
        # build psuedo header using source ip, destination ip, Zero = 0x00, PTLC = 0x06
        pseudo_header = ip_to_bytes(source_ip) + ip_to_bytes(dest_ip) + b'\x00\x06'

    # read the tcp_data file
    with open(tcp_filename, 'rb') as tcp_file:
        tcp_data = tcp_file.read()
        tcp_length = len(tcp_data)

        # convert the TCP length to a two-byte big-endian representation
        tcp_length_bytes = tcp_length.to_bytes(2, byteorder='big')

        pseudo_header += tcp_length_bytes

        checksum = calculate_checksum(pseudo_header, tcp_data)

        # extract the checksum from the original data in tcp_data file located "at byte offsets 16 and 17 inside the TCP header"
        # ref: 16.6 The TCP Header Checksum from "Reference" (see header)
        original_checksum = int.from_bytes(tcp_data[16:18], 'big')

        # compare the two checksums
        if checksum == original_checksum:
            print('PASS')
        else:
            print('FAIL')

# checking file path when debugging
import os
current_directory = os.getcwd()
print("Current directory:", current_directory)
os.chdir("/Users/bennetthamilton/Desktop/CS372/Projects/Project4")

# iterate through all files
for i in range(10):
    ip_filename = f'tcp_addrs_{i}.txt'
    tcp_filename = f'tcp_data_{i}.dat'
    print(f'Test {i+1}: ', end='')
    validate_tcp_packet(ip_filename, tcp_filename)