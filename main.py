import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["crud"]
print(mydb)
dblist = myclient.list_database_names()


mycol = mydb["customers"]
print(mycol)

mydict = { "name": "John", "address": "Highway 37" }
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

# x = mycol.insert_one(mydict)
# x=mycol.insert_many(mylist)
# print(x.inserted_ids)

# print(x)

# x = mycol.find_one()
# x=mycol.find()
# print(x)
# return only some field
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)



myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)
