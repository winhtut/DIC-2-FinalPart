import pymongo


class NccAuctionModel:
    def __init__(self):
        pass

    def connect(self, col_name):
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection["ncc_dip2"]
        collection = database[col_name]
        return collection

    def item(self):
        collection = self.connect("items_and_prices")

        return collection

    def candidate(self):
        collection = self.connect("candidate")
        return collection

    def user_info(self):
        collection = self.connect("user_info")
        return collection

    def info(self):
        collection = self.connect("info")
        return collection
