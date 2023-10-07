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
    # ref: https://www.geeksforgeeks.org/effect-of-b-character-in-front-of-a-string-literal-in-python/

    response = b""              # create and empty byte string to append response date

    while True:                 # continously receive data until there is none left
        data = s.recv(4096)     # receive up to 4096 bytes at a time
        if len(data) == 0:      # if there is no more data exit loop
            break
        response += data        # otherwise append data to response

    # close connection when all done
    s.close()

# call function
# ref: https://www.geeksforgeeks.org/command-line-arguments-in-python/

arg_len = 2         # define length of arguments
port = 80           # always default to port 80 (for now)

# assigning website
if len(sys.argv) < arg_len:
    # default to example.com 
    website = "example.com"
else:
    # otherwise use given website address
    website = sys.argv[1]

# call function
request_webpage(website, port)