CS372 Networking Project 3 - Word Server

This is a project that is all about reading packets.

You’ll receive a stream of encoded data from a server (provided) and you’ll have to write code to determine when you’ve received a complete 
packet and the print out that data.

RESTRICTION! Do not modify any of the existing code! Just search for TODO and fill in that code. You may add additional functions and 
variables if you wish.

REQUIREMENT! The code should work with any positive value passed to recv() between 1 and 4096! You might want to test values like 1, 5, and 
4096 to make sure they all work.

REQUIREMENT! The code must work with words from length 1 to length 65535. The server won’t send very long words, but you can modify it to 
test. To build a string in Python of a specific number of characters, you can: