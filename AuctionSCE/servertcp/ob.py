# This is ob program for servertcp and client actions
class Ob:
    def __init__(self):
        print("Starting OB Program!")


    def logging(self,data):
        pass

    def get_received(self,data):
        print("Received",data)
        return data


    def send_data(self,data):
        print("Sent:",data)
        return data


    def test_def(self,data):
        if data=="info":
            to_send = data+data
            return to_send
        else:
            return 'Nothing'