__author__ = 'asee2278'

import sys

try :
    print 5 /0
except Exception as e :
    print 'life sucks' , type(e) , e

print 'But life goes on '