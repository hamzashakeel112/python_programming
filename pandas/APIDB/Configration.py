# this file is for configure the conectionstring
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://hamzashakeel_db_user:H%40mza70126605@cluster0.kpci5gc.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection

# blow is name of culstor/database
db=client.todo_db   

# blow is the name of collection/table
# we can create multiple collection here

collection=db["todo_data"]



# db=client.Hospitalsite
# collection=db["multiple table"]
# db=client.Ecommerance
# collection=db["Item"]

# db=client.seller
# collection=db["sellertable 1"]

# db=client.company
# collection=db["seller"]

# db=client.databasename
# collection=db["database table"]

# db=client.databasename
# collection=db["database table"]

# db=client.databaseName
# collection=db["table name"]

# db=client.databaseName
# collection=db["table name"]

# db=client.databaseName
# collection=db["table name"]