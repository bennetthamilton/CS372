# Title: Project 2 - Better Server
# Name: Bennett Hamilton
# Date: 10/14/23
# Description: a better web server that is able to receive a get
#              request from client for a txt/html file, and respond
#              with contents of txt/html file

# imports
import sys
import socket
import os

# function to receive request data from connected client, returns request as a byte string
def receive_request(client_socket):
    request = b""                       # create and empty byte string to append request data
    while True:                         # continously receive data until there is none left
        data = client_socket.recv(1024)
        # break loop when there is not data
        if not data:
            break
        request += data                 # append data to request
        # if blank line delimiting the end of the header detected, break loop
        if b"\r\n\r\n" in request:
            break

    return request                       # return request as a byte string

# function to parse request header to get file name, strips path, returns only the file name
def parse_request_header(request):

    # parse header
    request_lines = request.split(b"\r\n")                  # split requests into seperate lines
    first_line = request_lines[0].decode()                  # get first line and decode into string   
    method, fullpath, protocol = first_line.split(" ")      # split first line into seperate sections

    # strip path from file to get the file name
    path_elements = fullpath.split("/")                     # split full path into seperate sections
    filename_list = path_elements[-1:]                      # last element will always be the file name
    filename_str = filename_list[0]                         # get the string element in list

    return filename_str                                     # return file name as a string

# build a response based on file type and contents, encode response, return response
# ref: https://docs.python.org/3/library/os.path.html#os.path.splitext
def build_response(filename_str):
    # determing the content type based on the file name
    name, file_type = os.path.splitext(filename_str)

    # map mime type to content type
    # ref: https://www.geeksforgeeks.org/switch-case-in-python-replacement/
    match file_type:
        case '.txt':
            content_type = 'text/plain'
        case '.html':
            content_type = 'text/html'
        case _:
            content_type = 'text/plain'

    # read data from filename
    try:
        # open and read the requested file
        with open(filename_str, "rb") as file:
            file_content = file.read()
        
        # Build the response with proper headers
        header = f"HTTP/1.1 200 OK\r\n"
        header += f"Content-Type: {content_type}\r\n"
        header += f"Content-Length: {len(file_content)}\r\n\r\n"
        response = header.encode() + file_content

        return response     # return encoded response
    
    except:
        # handle file not found or other error with 404 response
        return "HTTP/1.1 404 Not Found\r\n\r\nFile not found.".encode()

# handler function for processing client request
# ref: https://beej.us/guide/bgnet0/html/split/project-a-better-web-server.html
def process_client_request(client_socket):
    print(f"Processing client request...")

    # receive request data from connected client
    request = receive_request(client_socket)
    print(f"Request received.")
    print(request.decode())

    # parse request header to get filename
    filename = parse_request_header(request)
    print(filename) # for debugging

    # build response from file
    response = build_response(filename)

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
PORT_DEFAULT = 33490    # default port number

# assigning port number
if len(sys.argv) < ARG_LEN:
    # default port number
    port_number = PORT_DEFAULT
else:
    # otherwise use given port number
    port_number = int(sys.argv[1])

# call function
run_server_response(port_number)
