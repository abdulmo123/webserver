I. Part 1
web server = networking server that sits on a physical server
    - waits for a request from client -> receives a request -> generates a response -> sends back to client

    - comm between client & server happens using HTTP protocol

    http://localhost:8888/hello
        
        http = HTTP protocol
        localhost = host name
        8888 = port
        hello = path

        ^ this is how you tell your browser the addr of the web server it needs to find to connect to and the page (path) on the server to fetch for you 

    - before browser can send HTTP request
        -- establish a TCP (transfer control protocol) connection w/ web server
        -- waits for server to send HTTP response back
        -- when browser receives response, it displays it

    - how client and server establish a TCP connection BEFORE sending HTTP requests/responses?
        -- use 'SOCKETS'
        -- in this ex: simulate browser manually by using telnet on cmd


    - how webserver works ...
        -- web server creates listening socket and starts accepting new connections in a loop
        -- client initiates a TCP connection, after successfully establishing it, client sends HTTP request to server
        -- server responds with HTTP response that gets displayed to user
        -- to establish TCP connection, client & servers use 'sockets'

II. Part 2 
Python Web Server Gate Interface (WSGI) -- pronounced 'wizgy' ...
- solves problem of being able to run web server with multiple web frameworks