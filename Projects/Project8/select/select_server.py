# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    # create a socket for the server

    # bind the socket to the given port

    # list to keep track of connected clients

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
