# Title: Project 4 - Validating a TCP Packet
# Name: Bennett Hamilton
# Date: 10/29/23
# Description: code that validates a TCP packet, making sure it hasn’t been corrupted in transit


# Read the tcp_addrs_0.txt file.

# Split the line in two, the source and destination addresses.

# function that converts the dots-and-numbers IP addresses into bytestrings.

# Read the tcp_data_0.dat file.

# function that generates the IP pseudo header bytes from the IP addresses from tcp_addrs_0.txt and the TCP length from the tcp_data_0.dat file.

# Build a new version of the TCP data that has the checksum set to zero.

# Concatenate the pseudo header and the TCP data with zero checksum.

# Compute the checksum of that concatenation

# Extract the checksum from the original data in tcp_data_0.dat.

# Compare the two checksums