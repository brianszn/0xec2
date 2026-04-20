import socket
from threading import Thread


class Listener:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None

    def create_socket(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print(f'Listening: {self.host}:{self.port}')

    def accept_connection(self):
        conn, adrr = self.socket.accept()
        print(f'Connection from: {adrr}')
        return conn, adrr
    
    def send_data(self, conn, data):
        try:
            conn.sendall(data.encode())
        except Exception as e:
            print(f'Error sending data: {e}')

    def receive_data(self, conn):
        try:
            data = conn.recv(4096)
            if not data:
                return None
            return data.decode(encoding = 'latin-1')
        except Exception as e:
            print(f'Error receiving data: {e}')
            return None
    
    def handle_client(self, conn, addr):

        def escutar():
            while True:
                data = self.receive_data(conn)
                if data is None:
                    print(f'Client {addr} disconnected')
                    break
                print(f'Received from {addr}: {data.strip()}\ncmd> ', end='', flush=True)

        Thread(target=escutar, daemon=True).start()

        try:
                        
            while True:
                cmd = input('cmd> ')
                if not cmd:
                    continue
                self.send_data(conn, cmd)
        except Exception as e:
            print(f'Error handling client {addr}: {e}')
            

        finally:
            conn.close()
            
            print(f'Connection with {addr} closed')
    
    

if __name__ == "__main__":

    listener = Listener('192.168.56.1', 9090)
    listener.create_socket()
    while True:
        conn, addr = listener.accept_connection()
        client_thread = Thread(target=listener.handle_client, args=(conn, addr))
        client_thread.daemon = True
        client_thread.start()


    





