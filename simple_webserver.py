import socket

HOST, PORT = '', 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = server_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """

    client_connection.sendall(http_response)
    client_connection.close()