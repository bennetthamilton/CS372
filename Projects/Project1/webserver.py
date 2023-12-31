# Title: Project 1 - Server
# Name: Bennett Hamilton
# Date: 10/8/23
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
    s.listen(5)
    print(f"Project 1 server listening on port {port}...")

    # accept new connection (continously run loop)
    while True:
        
        new_conn = s.accept()       # accept new connection (tuple)
        new_socket = new_conn[0]    # assign to new socket
        print(f"Accepted connection")

        # receive request data from connected client
        request = b""               # create and empty byte string to append request data
        while True:                 # continously receive data until there is none left
            data = new_socket.recv(1024)
            # break loop when there is not data
            if not data:
                break
            request += data         # append data to request
            # if blank line delimiting the end of the header detected, break loop
            if b"\r\n\r\n" in request:
                break

        # build response
        response = (
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: 6\r\n"
            b"Connection: close\r\n\r\n"
            b"Hello!"
        )

        # send response
        new_socket.sendall(response)

        # close new socket
        new_socket.close()

        # loop back to accept new connection
    

# define constants
ARG_LEN = 2             # length of arguments
PORT_DEFAULT = 28333    # default port number

# assigning port number
if len(sys.argv) < ARG_LEN:
    # default port 
    port_number = PORT_DEFAULT
else:
    # otherwise use given port
    port_number = int(sys.argv[1])

# call function
run_server_response(port_number)
