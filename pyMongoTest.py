__author__ = 'premaseem'

import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']


doc = {'firstname':'Andrewa', 'lastname':'Erlichson'}
print doc
print "about to insert the document"

try:
    names.insert(doc)
except Exception as e:
    print "insert failed:", e