

import socket
class Session:
    
    def __init__(self, session_id, conn: socket.socket, addr):
        
        self.id = session_id
        self.conn = conn
        self.addr = addr
        self.hostname = "undefined"
        self.is_active = True
    
    def send_command(self, cmd):
        """Enviar um comando para a sessão"""
        from Listener import Listener
        try:
            
            Listener.send_data(self.conn, cmd)
        except Exception as e:
            self.is_active = False
            self.conn.close()
            print('send_command', e)

    def start_listener(self):
        from Listener import Listener
        while self.is_active:
            try:

                data = Listener.receive_data(self.conn)

                if not data:
                    print(f'\n[id: {self.id}] - die.')
                    self.is_active = False
                    break

                print(f'\n[id: {self.id}] Response: {data}') 
                print('cmd_principal: ', end='', flush=True)

            except Exception as e:
                self.is_active = False
                self.conn.close()
                print('start_listener', e)
                break
        
    
    def close_connection(self):

        print(f'Closing {self.addr[0]}...')
        self.is_active = False
        self.conn.close()

    