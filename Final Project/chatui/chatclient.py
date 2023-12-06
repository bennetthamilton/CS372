# Title: Final Project - Chat Client
# Name: Bennett Hamilton
# Date: 12/6/23
# Description: implementation of a chat client as specified by Project: Multiuser Chat Client and Server
#              ref: https://beej.us/guide/bgnet0/html/split/project-multiuser-chat-client-and-server.html

import socket
import threading
import json
from chatui import init_windows, read_command, print_message, end_windows

def run_client(nick, server_address, server_port):
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