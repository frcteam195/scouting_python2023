import argparse
import sys
import configparser

configParser = configparser.ConfigParser()
configParser.read("dbLogin.ini")

optionsDict = {}
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
    options = configParser.options(database)
    for option in options:
        try:
            optionsDict[option] = configParser.get(database, option)
            if optionsDict[option] == -1:
                DebugPrint("skip %s" % option)
        except:
                print("exception on %s!" % option)
                optionsDict[option] = None

def getdict():
    global optionsDict
    return optionsDict
