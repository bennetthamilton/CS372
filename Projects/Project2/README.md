Project 2: A Better Web Server

In this project we will build a web server that is able to recieve a get request for a
.html or .txt file, and then respond with the contents of that file to the client.

If you go to your browser and enter a URL like this (substituting the port number of your running server):

http://localhost:33490/file1.txt
The client will send a request to your server that looks like this:

GET /file1.txt HTTP/1.1
Host: localhost
Connection: close
Notice the file name is right there in the GET request on the first line!

Your server will:

Parse that request header to get the file name.
Strip the path off for security reasons.
Read the data from the named file.
Determine the type of data in the file, HTML or text.
Build an HTTP response packet with the file data in the payload.
Send that HTTP response back to the client.
The response will look like this example file:

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 357
Connection: close

...
[The rest of the HTML file has been truncated in this example.]

At this point, the browser should display the file.

Notice a couple things in the header that need to be computed: the Content-Type will be set according 
to the type of data in the file being served, and the Content-Length will be set to the length in bytes of that data.

We're going to want to be able to display at least two different types of files: HTML and text files.