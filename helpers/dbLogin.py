import argparse
import sys
import configparser

c = configparser.ConfigParser()
c.read("dbLogin.ini")

dict1 = {}
database = ""

def login(db):
    global database
    global dict1
    if db == "aws-prod":
        database = "aws-prod"
    elif db == "aws-dev":
        database = "aws-dev"
    elif db == "pi-10":
        database = "pi-10"
    elif db == "pi-192":
        database = "pi-192"
    elif db == "localhost":
        database = "localhost"
    else:
        print(db + " is not a valid database choice, see --help for choices")
        sys.exit()

    print("Connecting to " + database)
    options = c.options(database)
    for option in options:
        try:
            dict1[option] = c.get(database, option)
            if dict1[option] == -1:
                DebugPrint("skip %s" % option)
        except:
                print("exception on %s!" % option)
                dict1[option] = None

def getdict():
    global dict1
    return dict1