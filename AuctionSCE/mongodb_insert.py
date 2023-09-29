from pymongo import MongoClient


# Connect to MongoDB
def connect_to_mongodb():
    try:
        # Replace 'mongodb://localhost:27017/' with your MongoDB connection string
        client = MongoClient('mongodb://localhost:27017/')
        return client
    except Exception as e:
        print("Error connecting to MongoDB:", str(e))


# Create a new document in a collection
def create_document(client, db_name, collection_name, document):
    try:
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_one(document)
        print("Document created with ID:", result.inserted_id)
    except Exception as e:
        print("Error creating document:", str(e))


# Read documents from a collection
def read_documents(client, db_name, collection_name):
    try:
        db = client[db_name]
        collection = db[collection_name]
        documents = collection.find()
        for document in documents:
            print(document)
    except Exception as e:
        print("Error reading documents:", str(e))


# Update a document in a collection
def update_document(client, db_name, collection_name, filter_query, update_query):
    try:
        db = client[db_name]
        collection = db[collection_name]
        result = collection.update_one(filter_query, update_query)
        print("Matched documents:", result.matched_count)
        print("Modified documents:", result.modified_count)
    except Exception as e:
        print("Error updating document:", str(e))


# Delete documents from a collection
def delete_documents(client, db_name, collection_name, filter_query):
    try:
        db = client[db_name]
        collection = db[collection_name]
        result = collection.delete_many(filter_query)
        print("Deleted documents count:", result.deleted_count)
    except Exception as e:
        print("Error deleting documents:", str(e))


# Usage
client = connect_to_mongodb()

# Create a document
db_name = 'ncc_dip2'
collection_name = 'items_and_prices'
document = {'name':"Bike-Adv-BMW",'reserve_price':500000}
create_document(client, db_name, collection_name, document)

# Read documents
read_documents(client, db_name, collection_name)

# # Update a document
# filter_query = {'name': 'John Doe'}
# update_query = {'$set': {'age': 35}}
# update_document(client, db_name, collection_name, filter_query, update_query)

# Delete documents
# delete_query = {'name': 'John Doe'}
# delete_documents(client, db_name, collection_name, delete_query)

# Close the MongoDB connection
client.close()
