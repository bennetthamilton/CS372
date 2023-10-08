# Title: Project 1 - Server
# Name: Bennett Hamilton
# Date: 10/7/23
# Description: practice setting up a web server on python

# imports
import sys
import socket

# main server function, send response after receiving request from client
def run_server_response(port):

    # get socket
    s = socket.socket()

    # bind socket
    s.bind(('', port))

    # listen for connection


    # accept new connection


    # receive request from client


    # build response


    # send response


    # close new socket


    # loop back to accept new connection

# define constants
ARG_LEN = 2             # length of arguments
PORT_DEFAULT = 28333    # default port number

# assigning port number
if len(sys.argv) < ARG_LEN:
    # default to example.com 
    port_number = PORT_DEFAULT
else:
    # otherwise use given website address
    website = sys.argv[1]

# call function
run_server_response(port_number)
