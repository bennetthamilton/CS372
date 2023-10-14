# Title: Project 2 - Better Server
# Name: Bennett Hamilton
# Date: 10/14/23
# Description: a better web server that is able to receive a get
#              request from client for a txt/html file, and respond
#              with contents of txt/html file

# imports
import sys
import socket

# function to receive request data from connected client, returns request as a byte string
def receive_request(client_socket):
    request_bstring = b""               # create and empty byte string to append request data
    while True:                 # continously receive data until there is none left
        data = client_socket.recv(1024)
        # break loop when there is not data
        if not data:
            break
        request_bstring += data         # append data to request
        # if blank line delimiting the end of the header detected, break loop
        if b"\r\n\r\n" in request_bstring:
            break

    return request_bstring

# handler function for processing client request
def process_client_request(client_socket):
    # receive request data from connected client
    request = receive_request(client_socket)

    # TODO parse request header to get filename

    # TODO strip off path (for security reasons)

    # TODO read data from filename

    # TODO determine content type (html/txt)

    # TODO build response from txt/html file
    response = ''

    # send response
    client_socket.sendall(response)

    # close new socket
    client_socket.close()

    # loop back to accept new connection in run function

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

        # receive request data from connected client, get file, and respond with file contents
        process_client_request(new_socket)
        
    

# define constants
ARG_LEN = 2             # length of arguments
PORT_DEFAULT = 28333    # default port number

# assigning port number
if len(sys.argv) < ARG_LEN:
    # default port number
    port_number = PORT_DEFAULT
else:
    # otherwise use given port number
    port_number = sys.argv[1]

# call function
run_server_response(port_number)
