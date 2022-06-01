import argparse
import sys
import configparser
import mariadb as mariaDB

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

if database == "aws-dev":
    print("Input database " + input_database)
    conn = mariaDB.connect(user='admin',
                                passwd='xxxx',
                                host='frcteam195testinstance.cmdlvflptajw.us-east-1.rds.amazonaws.com',
                                database='team195_scouting')
    cursor = conn.cursor()
        
elif database == "pi-10":
    conn = mariaDB.connect(user='admin',
                            passwd='xxxx',
                            host='10.0.20.195',
                            database='team195_scouting')
    cursor = conn.cursor()
        
elif database == "pi-192":
    conn = mariaDB.connect(user='admin',
                            passwd='xxxx',
                            host='192.168.1.195',
                            database='team195_scouting')
    cursor = conn.cursor()

elif database == "localhost":
    conn = mariaDB.connect(user='admin',
                            passwd='xxxx',
                            host='localhost',
                            database='team195_scouting')
    cursor = conn.cursor()

elif database == "aws-prod":
    conn = mariaDB.connect(user='admin',
                            passwd='xxxx',
                            host='frcteam195.cmdlvflptajw.us-east-1.rds.amazonaws.com',
                            database='team195_scouting')
    cursor = conn.cursor()

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