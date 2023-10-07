# Title: Project 1 - Client
# Name: Bennett Hamilton
# Date: 10/7/23
# Description: prectice setting up a web client on python

# imports
import socket

# init variiables
website = "example.com"
port = 80

# ask OS for socket, assign to variable
s = socket.socket()

# connect the socket (skip DNS lookup)
s.connect(website, port)

# send and recieve data

# close connection
s.close()