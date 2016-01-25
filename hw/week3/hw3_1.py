__author__ = 'asee2278'

import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.test4
students = db.students


def find():

    print "find, reporting for duty"

    query = {}
#    projection = {'student_id':1, '_id':0}
#    projection = {'student_id':1, '_id':0,'score':1 }

    try:
        cursor = students.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        original_score = doc['scores']
        score_to_remove = {}
        score_to_add = {}
        #print original_score

        subDocType1 = original_score[2]
        subDocType2 = original_score[3]
        print doc

        if subDocType1['score'] >  subDocType2['score'] :
            #score_to_remove = subDocType2['score']
            #score_to_add = subDocType1['score']
            original_score.remove(subDocType2)
            print score_to_remove
        else :
            #score_to_remove = subDocType1['score']
            #score_to_add = subDocType2['score']
            original_score.remove(subDocType1)

        print 'doc with score to remove '
        # doc['scores'].remove(score_to_remove)
        print doc
        id = doc['_id']
        result = students.update_one({'_id':id},
                          {'$set':{'scores': original_score}})

        sanity += 1
        #if (sanity > 1):
        #    break


find()
