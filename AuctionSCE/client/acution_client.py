import socket
import encry_decrypt
from colorama import Fore


class Auction_client():

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9191
        self.userKey = self.getting_key()
        self.client_menu()

    def getting_key(self):
        userKey: str = input("Enter your encryption key for the whole process:")
        return userKey

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client  # to send and received data

    def client_menu(self):
        print("This is client menu:")
        user_data = input("'get:Get_all_information\n"'login:to login''reg:to register'
                          "'Press 1 to get auction info:\nPress 2 To Exit:")
        client = self.client_runner()
        if user_data == '1':
            raw_data: str = 'info'
            self.sending_encrypted(client, raw_data)

        elif user_data == 'login':
            self.login(client)

        elif user_data == 'reg':
            pass

        elif user_data == 'get':
            pass

    def sending_encrypted(self, client, raw_data: str):
        encry = encry_decrypt.A3Encryption()
        decry = encry_decrypt.A3Decryption()
        encrypted_data = encry.start_encryption(raw_data, self.userKey)
        client.send(bytes(encrypted_data, "utf-8"))
        recv_info = client.recv(4096)
        recv_encrypted = recv_info.decode("utf-8")
        print("Received Encrypted Data : ", recv_encrypted)

        recv_decrypted = decry.startDecryption(recv_encrypted)
        client.close()
        return recv_decrypted

    def login(self, client):
        space = ' '
        global l_email, l_pass
        try:
            l_email = input("Enter your user email to Login:")
            l_pass = input("Enter your password:")
        except Exception as err:
            print("Invalid Input ")
            try:
                check = int(input("Press 1 to login again:\nPress 2 to Menu:"))
                if check == 1:
                    self.login(client)
                else:
                    self.client_menu()
            except Exception as err:
                print(err)
                self.login(client)

        raw_data = 'login' + space + l_email + space + l_pass
        # we got decrypted data from server
        de_from_server = self.sending_encrypted(client, raw_data)
        de_from_server = de_from_server.split(' ')

        if de_from_server[0] == 'login' and de_from_server[1] == l_email and de_from_server[2] == l_pass:
            print("Login Success")
            self.boss_sector(de_from_server)
        else:
            print("Login Failed")
            try:
                check = int(input("Press 1 to login again:\nPress 2 to Menu:\nPress 3 to Register:"))
                if check == 1:
                    self.login(client)
                elif check == 2:
                    self.client_menu()
                else:
                    self.register()
            except Exception as err:
                self.client_menu()

    def register(self):
        print("This is register:")

    def boss_sector(self, boss_data):
        client = self.client_runner()
        # print("data:",boss_data)
        # print("data type",type(boss_data))
        print("Hello Boss...")
        print("[+]Welcome Sir:", boss_data[1])
        print("Your Point:", boss_data[-1])
        try:
            option = int(input("[+]1: Add Points:\n[+]2:Transfer Points:\n[+]3:Make Auction:\n[+]4:Change Info"
                               "\n[+]5:Get Auction items list:\n[+]6:Today Auction History:\n[X]:7 For Exit:\n[+]:Enter Here->:"
                               ""))
            print("Boss Option:",option)
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                raw_msg = "auction " + boss_data[1]
                received_data = self.sending_encrypted(client, raw_msg)
                received_data = received_data.split(' ')

                if int(received_data[1]) >= 50:
                    print("U can make Auction")
                else:
                    print("Please make more Points:\n")
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

            else:
                pass
        except Exception as err:
            print(err)
            self.boss_sector(boss_data)


if __name__ == "__main__":
    auction_client: Auction_client = Auction_client()

    while True:
        auction_client.client_menu()
