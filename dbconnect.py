import MySQLdb
import getpass
import os
import _strptime

from pip._vendor.distlib import database


def connect():
    print "Enter Host"
    host = raw_input()

    print "Enter Database"
    database = raw_input()

    print "Enter User"
    user = raw_input()

    print "Enter Password"
    password = getpass.getpass()





 MySQLdb.connect(host=host, database=database, user=user, password=password)


connect()
