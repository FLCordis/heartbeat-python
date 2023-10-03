import socket
import time

def start_client():
    host = 'localhost'
    port = 12345
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Cliente conectado ao servidor!")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Recebendo dados do servidor: " + str(data))
            message = 'PONG'
            client_socket.send(message.encode())
            time.sleep(1)
        except socket.error:
            print("Servidor inativo!.")
            break
    client_socket.close()

if __name__ == '__main__':
    start_client()
