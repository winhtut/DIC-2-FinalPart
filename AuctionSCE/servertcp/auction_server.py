import socket
import s_encrypt_and_decrypt
import ob
from dbModel import NccAuctionModel


class Server():

    def __init__(self):

        self.ob = ob.Ob()
        self.decrypt = s_encrypt_and_decrypt.A3Decryption()
        self.encrypt = s_encrypt_and_decrypt.A3Encryption()
        self.server_ip = "localhost"
        self.server_port = 9191
        self.rc: RequestControl = RequestControl()

    def main(self):

        auction_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        auction_server.bind((self.server_ip, self.server_port))

        auction_server.listen()

        print("Server listen on port:{} and ip{}".format(self.server_port, self.server_ip))

        try:
            while True:
                client, address = auction_server.accept()
                print("Accepted Connection from -{} : {}".format(address[0], address[1]))

                self.client_control(client)

        except Exception as err:
            print(err)

    def client_control(self, client):

        with client as sock:
            from_client = sock.recv(1024)

            data_list = from_client.decode("utf-8")

            decrypted = self.decrypt.startDecryption(data_list)
            print("#:", decrypted)
            decrypted_list = decrypted.split(' ')
            # ob_recv = self.ob.get_received(decrypted_list[0])
            # print("Ob data:", ob_recv)

            data = ''
            if decrypted_list[0] == 'info':
                '''
                this code for test ob server 
                '''
                to_send = self.ob.test_def(decrypted_list[0])
                if to_send == 'info':
                    data = self.rc.info(decrypted_list)
                else:
                    data = 'Observer-not-permit'

            #
            elif decrypted_list[0] == 'login':
                print("1-login check!")
                '''
                This is login 
                '''
                data = self.rc.login(decrypted_list)

            elif decrypted_list[0] == 'auction':

                print("Auction check!")
                '''
                Auction checking
                '''
                data = self.rc.auction_check(decrypted_list)

            encrypted = self.encrypt.start_encryption(data, 'servertcp')

            sock.send(bytes(encrypted, "utf-8"))

            ob_send = self.ob.send_data(data)
            print("Ob send:", ob_send)

    # def for_observer(self):
    #     # to_return = self.decrypted_data
    #     #
    #     # self.decrypted_data='n'
    #     return self.decrypted_data


class RequestControl:
    def __init__(self):
        self.database = NccAuctionModel()

    def info(self, dataList):

        collection = self.database.info()
        doc = ''
        for i in collection.find({}, {"_id": 0}):
            print(i)
            doc += i['info']
        return doc

    def login(self, dataList):
        collection = self.database.user_info()

        toReturn = 'nothing'
        print("2-server login checking")
        try:
            for i in collection.find({}, {'_id': 0}):
                print(i['email'], i['password'])
                if i['email'] == dataList[1] and i['password'] == dataList[2]:
                    toReturn = 'login' + ' ' + i['email'] + ' ' + i['password'] + ' ' + str(i['phone']) + ' ' + i[
                        'info'] + ' ' + str(i['point'])
        except Exception as err:
            toReturn = 'Db checking error '
            print("db checking error")
        print("3-toReturn", toReturn)
        return toReturn

    def register(self, dataList):
        return dataList

    def auction_check(self, dataList):

        collection = self.database.user_info()
        point = 0
        for i in collection.find({},{'email': 1, 'point': 1}):

            if dataList[1] == i['email']:
                point = i['point']
        toReturn = dataList[0] + ' ' + str(point)
        return toReturn


if __name__ == "__main__":
    auction: Server = Server()
    auction.main()
