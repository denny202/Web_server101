import socket

class Webserver:
    # Initialise
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        #create socket object (IPV4 / TCP)
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #allows usage of same address
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind addr and port
        self.listen_socket.bind((self.host, self.port))
        #start listening and queue only 1 max number of connections
        self.listen_socket.listen(1)
        print(f'Serving HTTP on port {self.port} ...')
    
    def serve_forever(self):
        #Listen in loop
        while True:
            # waits for conns and return socket object
            client_conn, client_addr = self.listen_socket.accept()
            #max bytes 1024 to read at once 
            request_data = client_conn.recv(1024)
            #decode to a string and print
            print(request_data.decode('utf-8'))
    
            http_response = b"""\
                                    HTTP/1.1 200 OK

                                    Serve the World!
                                    """
            client_conn.sendall(http_response)
            client_conn.close()

if __name__ == "__main__":
    server = Webserver('', 8080)
    server.serve_forever()
