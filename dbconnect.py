import mysql
import getpass
import os
import _strptime


def connect ():
    print "Enter User"
    user = raw_input()

    print "Enter Password"
    password = raw_input(getpass.getpass)

connect()