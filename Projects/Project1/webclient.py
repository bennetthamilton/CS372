# Title: Project 1 - Client
# Name: Bennett Hamilton
# Date: 10/7/23
# Description: prectice setting up a web client on python

# imports
import socket
import sys

def request_webpage(website, port)
    # ask OS for socket, assign to variable
    s = socket.socket()

    # connect the socket (skip DNS lookup)
    s.connect(website, port)

    # build request (using provided example)
    request = f"GET / HTTP/1.1\r\nHost: {website}\r\nConnection: close\r\n\r\n"

    # send data
    s.sendall(request.encode("ISO-8859-1"))

    # recieve data

    # close connection
    s.close()

# call function
# ref: https://www.geeksforgeeks.org/command-line-arguments-in-python/

arg_len = 2     # define length of arguments
port = 80       # always default to port 80 (for now)

# assigning website
if len(sys.argv) < arg_len:
    # default to example.com 
    website = "example.com"
else:
    # otherwise use given website address
    website = sys.argv[1]

# call function
request_webpage(website, port)