# Title: Final Project - Chat Server
# Name: Bennett Hamilton
# Date: 12/6/23
# Description: implementation of a chat server as specified by Project: Multiuser Chat Client and Server
#              ref: https://beej.us/guide/bgnet0/html/split/project-multiuser-chat-client-and-server.html

import sys
import socket
import select
import json

# ref: CS372/Projects/Project8/select/select_server.py
# ref: https://beej.us/guide/bgnet0/html/split/select.html
def run_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    read_set = [server_socket]
    clients = {}

    print("Waiting for connections...")

    while True:
        ready_to_read, _, _ = select.select(read_set, {}, {})

        for s in ready_to_read:
            if s is server_socket:  # if socket is a listening socket, accept new connection
                client_socket, client_address = server_socket.accept()
                read_set.append(client_socket)
                clients[client_socket] = {'nick': None, 'buffer': b''}   # add info to client dictionary
                print("*** New client connected")

            else:  # socket is a regular socket, receive data and process data from an existing client
                data = s.recv(1024)
                if not data:        
                    handle_client_disconnect(s, clients)
                    read_set.remove(s)
                else:
                    handle_client_data(s, data, clients)


# ref: https://beej.us/guide/bgnet0/html/split/parsing-packets.html
def handle_client_data(sock, data, clients):
    client_info = clients[sock]
    client_info['buffer'] += data

    while True:
        packet, remaining_data = extract_packet(client_info['buffer'])
        if packet is None:
            break

        handle_packet(sock, packet, clients)
        client_info['buffer'] = remaining_data


# ref: https://beej.us/guide/bgnet0/html/split/parsing-packets.html
# ref: https://beej.us/guide/bgnet0/html/split/appendix-json.html
def extract_packet(buffer):
    if len(buffer) < 2:
        return None, buffer

    payload_length = int.from_bytes(buffer[:2], 'big')

    if len(buffer) < payload_length + 2:
        return None, buffer

    payload_data = buffer[2:payload_length + 2].decode('utf-8')
    remaining_data = buffer[payload_length + 2:]

    return json.loads(payload_data), remaining_data


def handle_packet(sock, packet, clients):
    packet_type = packet.get('type')

    if packet_type == 'hello':
        handle_hello_packet(sock, packet, clients)
    elif packet_type == 'chat':
        handle_chat_packet(sock, packet, clients)


def handle_hello_packet(sock, packet, clients):
    clients[sock]['nick'] = packet.get('nick')
    broadcast_join_message(sock, clients)


def handle_chat_packet(sock, packet, clients):
    sender_nick = clients[sock]['nick']
    message = packet.get('message')
    broadcast_chat_message(sender_nick, message, clients)


def broadcast_join_message(sock, clients):
    sender_nick = clients[sock]['nick']
    join_packet = {'type': 'join', 'nick': sender_nick}
    broadcast(sock, join_packet, clients)


def broadcast_chat_message(sender_nick, message, clients):
    chat_packet = {'type': 'chat', 'nick': sender_nick, 'message': message}
    broadcast(None, chat_packet, clients)


def broadcast(sender_sock, packet, clients):
    # broadcast to everyone except the sender
    for client_sock in clients:
        if client_sock != sender_sock:
            send_packet(client_sock, packet)


def send_packet(sock, packet):
    # create payload
    payload_data = json.dumps(packet).encode('utf-8')
    payload_length = len(payload_data).to_bytes(2, 'big')
    sock.send(payload_length + payload_data)    # send to socket


def handle_client_disconnect(sock, clients):
    if sock in clients:
        sender_nick = clients[sock]['nick']            # store nickname
        del clients[sock]                              # remove client
        broadcast_leave_message(sender_nick, clients)  # broadcast to other clients


def broadcast_leave_message(sender_nick, clients):
    leave_packet = {'type': 'leave', 'nick': sender_nick}
    broadcast(None, leave_packet, clients)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python chat_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    run_server(port)