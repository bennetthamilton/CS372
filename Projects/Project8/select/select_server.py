# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    # create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to the given port
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    # list to keep track of connected clients
    clients = [server_socket]

    print("waiting for connections")

    # processing loop
        # select ready to read sockets
        # for each sockets
            # if listening socket
                # accept new connection
            # else
                # receive data
                # if no more data
                    # close connection
                # else
                    # print length and raw data received
    pass

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
