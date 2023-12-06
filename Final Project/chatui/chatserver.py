# Title: Final Project - Chat Server
# Name: Bennett Hamilton
# Date: 12/6/23
# Description: implementation of a chat server as specified by Project: Multiuser Chat Client and Server
#              ref: https://beej.us/guide/bgnet0/html/split/project-multiuser-chat-client-and-server.html

import sys
import socket
import select

# ref: CS372/Projects/Project8/select/select_server.py
def run_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    read_set = [server_socket]
    clients = {}

    print("waiting for connections")

    while True:
        ready_to_read, _, _ = select.select(read_set, {}, {})

        for s in ready_to_read:
            if s is server_socket:  # if socket is a listening socket, accept new connection
                client_socket, client_address = server_socket.accept()
                read_set.append(client_socket)
                # add to client dictionary
                clients[client_socket] = {'nick': None, 'buffer': ''}
                print("*** New client connected")

            else:  # socket is a regular socket, receive data and process data from an existing client
                data = s.recv(1024)
                if not data:        
                    handle_client_disconnect(s, clients)
                    read_set.remove(s)
                else:
                    handle_client_data(s, data, clients)

def handle_client_data(sock, data, clients):
    pass

def handle_client_disconnect(sock, clients):
    pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python chat_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    run_server(port)