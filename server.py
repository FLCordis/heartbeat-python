import socket
import time

def start_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor Heartbeat iniciado com sucesso!")
    while True:
        conn, address = server_socket.accept()
        print("Conexão de: " + str(address) + "iniciada!")
        while True:
            try:
                message = 'PING'
                conn.send(message.encode())
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Recebendo resposta do Cliente: " + str(data))
                time.sleep(1)
            except socket.error:
                print("Cliente " + str(address) + " desconectado.")
                break
        conn.close()

if __name__ == '__main__':
    start_server()
