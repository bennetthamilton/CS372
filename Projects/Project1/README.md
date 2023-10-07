Project 1: Web Client and Server

Introduction
We're going to write a sockets program that can download files from a web server! This is 
going to be our "web client". This will work with almost any web server out there, if we 
ode it right.

And as if that's not enough, we're going to follow it up by writing a simple web server! 
This program will be able to handle requests from the web client we write... or indeed 
any other web client such as Chrome or Firefox!

These programs are going to speak a protocol you have probably heard of: HTTP, the 
HyperText Transport Protocol.

And because they speak HTTP, and web browsers like Chrome speak HTTP, they should be able 
to communicate!

Restrictions
In order to better understand the sockets API at a lower level, this project may not use 
any of the following helper functions:

The socket.create_connection() function.
The socket.create_server() function.
Anything in the urllib modules.
After coding up the project, it should be more obvious how these helper functions are 
implemented.