# Title: Project 3 - Atomic Time
# Name: Bennett Hamilton
# Date: 10/21/23
# Description: reach out to the atomic clock at NIST (National Institute of Standards and Technology) 
#              and get the number of seconds since January 1, 1900 from their clocks.

# ref: https://beej.us/guide/bgnet0/html/split/project-atomic-time.html

import socket
import time

def connect():
    nist_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nist_socket.connect(("time.nist.gov", 37))

def main():
    # connect to nst server
    connect()

    # receive 4 bytes of time data

    # decode bytes

    # print out nst time value

    # print out system time value

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

if __name__ == "__main__":
    main()