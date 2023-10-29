# Title: Project 4 - Validating a TCP Packet
# Name: Bennett Hamilton
# Date: 10/29/23
# Description: code that validates a TCP packet, making sure it hasn’t been corrupted in transit
# Reference: https://beej.us/guide/bgnet0/html/split/project-validating-a-tcp-packet.html



# function that converts the dots-and-numbers IP addresses into bytestrings
# ref: https://www.geeksforgeeks.org/python-map-function/
# ref: https://www.w3schools.com/python/ref_string_split.asp
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
        # function that generates the IP pseudo header bytes from the IP addresses from tcp_addrs_0.txt

    # read the tcp_data file
    with open(tcp_filename, 'rb') as tcp_file:
        tcp_data = tcp_file.read()
        tcp_length = len(tcp_data)
        # function that generates the TCP length from the tcp_data_0.dat file.
    

    # Build a new version of the TCP data that has the checksum set to zero.

    # Concatenate the pseudo header and the TCP data with zero checksum.

    # Compute the checksum of that concatenation

    # Extract the checksum from the original data in tcp_data_0.dat.

    # Compare the two checksums