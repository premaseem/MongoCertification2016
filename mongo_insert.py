

import pymongo
import sys


connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Andrewa', 'lastname':'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except Exception as e:
    print "insert failed:", e

print doc
doc = {'firstname':'Andrewa', 'lastname':'Erlichson'}
print "inserting again"

try:
    users.insert(doc)
except Exception as e:
    print "second insert failed:", e

print doc

