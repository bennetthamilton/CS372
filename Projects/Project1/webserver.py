# Title: Project 1 - Server
# Name: Bennett Hamilton
# Date: 10/7/23
# Description: practice setting up a web server on python

# imports
import sys
import socket

# get socket
s = socket.socket()

# define constants
ARG_LEN = 2             # length of arguments
PORT_DEFAULT = 28333    # default port number

# assigning port number
if len(sys.argv) < ARG_LEN:
    # default to example.com 
    port = PORT_DEFAULT
else:
    # otherwise use given website address
    website = sys.argv[1]

# call function
