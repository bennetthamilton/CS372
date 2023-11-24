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
    read_set = {server_socket}

    print("waiting for connections")

    # processing loop
    while True:
        # select ready to read sockets
        ready_to_read, _, _ = select.select(read_set, {}, {})
        for s in ready_to_read:
            if s is server_socket:  # socket is a listening socket
                # accept new connection
                client_socket, client_address = server_socket.accept()
                read_set.append(client_socket)

                print(f'{client_address}: connected')
            else:                   # socket is a regular socket
                # receive data and process data from an existing client
                data = s.recv(1024)
                if not data:        # data = 0 bytes
                    # close connection
                    print(f'{s.getpeername()}: disconnected')
                    s.close()
                    read_set.remove(s)
                else:
                    # print length and raw data received
                    print(f'{s.getpeername()} {len(data)} bytes: {data}')

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
