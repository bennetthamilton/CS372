CS372 Project 3: Atomic Time

The is what we’ll be doing:

1. Connect to the server time.nist.gov on port 37 (the Time Protocol port).

2. Receive data. (You don’t need to send anything.) You should get 4 bytes.

3. The 4 bytes represent a 4-byte big-endian number. Decode the 4 bytes with .from_bytes() into a numeric variable.

4. Print out the value from the time server, which should be the number of seconds since January 1, 1900 00:00.

5. Print the system time as number of seconds since January 1, 1900 00:00.

The two times should loosely (or exactly) agree if your computer’s clock is accurate.

The number should be a bit over 3,870,000,000, to give you a ballpark idea. And it should increment once per second.