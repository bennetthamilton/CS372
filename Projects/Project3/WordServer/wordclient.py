# Title: Project 3 - Word Client
# Name: Bennett Hamilton
# Date: 10/21/23
# Description: practice using a word client to send and receive packets of data

import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

# ref: https://beej.us/guide/bgnet0/html/split/parsing-packets.html#parsing-packets
def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    global packet_buffer

    # read bytes to determine the word length
    while len(packet_buffer) < WORD_LEN_SIZE:
        # receive data from socket
        data = s.recv(WORD_LEN_SIZE - len(packet_buffer))
        # close connection when there is no more data
        if not data:
            return None
        packet_buffer += data

    # extract the word length from the packet buffer
    word_len = int.from_bytes(packet_buffer[:WORD_LEN_SIZE], byteorder='big')
    packet_buffer = packet_buffer[WORD_LEN_SIZE:]

    print(f"Word length: {word_len}")

    # read enough bytes to complete the word packet
    while len(packet_buffer) < word_len:
        data = s.recv(word_len - len(packet_buffer))
        if not data:
            return None 
        packet_buffer += data

    # extract complete word packet
    word_packet = packet_buffer[:word_len]      # grab the packet
    packet_buffer = packet_buffer[word_len:]    # slice it off the front

    print(f"Word packet: {word_packet}")

    return word_packet


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """

    # extract the word (excluding the length bytes)
    word = word_packet[WORD_LEN_SIZE:]

    # decode the word using UTF-8 encoding
    word = word.decode()

    return word

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))