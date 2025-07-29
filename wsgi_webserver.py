import io
import socket
import sys

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__ (self, server_address):
        # create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )

        # allow to reuse same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # bind 
        listen_socket.bind(server_address)

        # activate 
        listen_socket.listen(self.request_queue_size)

        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port

        # return headers set by web framework/web app
        self.headers_set = []

    
    def set_app(self, app):
        self.app = app
    

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            # new client connection
            self.client_connection, client_address = listen_socket.accept()

            # handle one request and close the client connection
            # then loop over to wait for another client connection
            self.handle_one_request()
    

    def handle_one_request(self):
        request_data = self.client_connection.recv(1024)
        self.request_data = request_data = request_data.encode('utf-8')

        # print formatted request data a la 'curl -v'
        print(''.join(
            f'< {line}\n' for line in request_data.splitlines()
        ))

        self.parse_request(request_data)

        # construct env dict using request data
        env = self.get_environ()
    
        # time to call our app callable and
        # get back result that will become HTTP resp body
        result = self.app(env, self.start_response)

        # construct response and send it back to client
        self.finish_response(result)