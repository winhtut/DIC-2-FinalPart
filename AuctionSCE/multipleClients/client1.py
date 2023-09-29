import socket

def main():
    host = "localhost"
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello Server!"

    try:
        while True:
            client_socket.send(message.encode('ascii'))
            data = client_socket.recv(1024)
            print(f'Received from server: {data.decode()}')
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
