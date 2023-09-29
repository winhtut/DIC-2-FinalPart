import socket
import threading
import time
from colorama import Fore

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        print(f"New connection added: {client_address}")

    def run(self):
        print(f"Connection from: {self.client_address}")
        while True:
            time.sleep(1)  # wait for 1 second
            message = f"Broadcast from server"
            print(Fore.RED+message)

            for client in clients:
                try:
                    client.send(message.encode())
                except:
                    clients.remove(client)
                    print(f"Client {self.client_address} has been removed")
        self.client_socket.close()

def main():
    global clients
    clients = []

    host = "localhost"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))

    print("Server started")
    print("Waiting for clients...")

    while True:
        server_socket.listen(1)
        client_sock, client_address = server_socket.accept()
        clients.append(client_sock)
        new_thread = ClientThread(client_address, client_sock)
        new_thread.start()

if __name__ == "__main__":
    main()
