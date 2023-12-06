# Title: Final Project - Chat Client
# Name: Bennett Hamilton
# Date: 12/6/23
# Description: implementation of a chat client as specified by Project: Multiuser Chat Client and Server
#              ref: https://beej.us/guide/bgnet0/html/split/project-multiuser-chat-client-and-server.html

import socket
import threading
import json
from chatui import init_windows, read_command, print_message, end_windows
from chatserver import send_packet


def run_client(nick, server_address, server_port):
    # init client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))

    # create hello packet and send
    hello_packet = {'type': 'hello', 'nick': nick}
    send_packet(client_socket, hello_packet)

    # create new client thread
    t1 = threading.Thread(target=receive_messages, args=(client_socket,))
    t1.start()

    while True:  # chat loop
        try: 
            message = read_command(f"{nick}> ")
            if message.startswith("/q"):    # special user input
                break  
            elif message.startswith("/"):   # other commands not supported
                print_message("Invalid command. Supported command: /q")
            else:                           # create packet and send
                chat_packet = {'type': 'chat', 'message': message}
                send_packet(client_socket, chat_packet)
        # ref: https://docs.python.org/3/library/exceptions.html
        except KeyboardInterrupt: 
            break
    
    client_socket.close()


def receive_messages(client_socket):
    pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python chat_client.py <nick> <server_address> <server_port>")
        sys.exit(1)

    nick = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])

    init_windows()
    run_client(nick, server_address, server_port)
    end_windows()