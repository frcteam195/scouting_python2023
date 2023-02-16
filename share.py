import mysql.connector
import tbapy
import sys
import getopt
import sys
import argparse
import configparser
import pandas as pd

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

CEventID = cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
CEventID = cursor.fetchone()[0]

query = "SELECT element from share WHERE share = 1"
cursor.execute(query)
elementList = (cursor.fetchall())
elements = str(elementList)
elements = elements.replace(",), (", ", ")
elements = elements.replace(elements[len(elements) - 3:], "")
elements = elements.replace(elements[0],"")
elements = elements.replace(elements[0],"")
elements = elements.translate(str.maketrans("", "", "'"))
# elements = (','.join(elements))

query = f"Select {elements} from matchScouting WHERE eventID = {CEventID}"
#print(query)
cursor.execute(query)
sharedData = cursor.fetchall()
#print(sharedData)

df = pd.DataFrame(sharedData)
#print(df)

headerList = []
print(elementList)
for i in elementList:
    i = str(i).translate(str.maketrans("", "", "(),"))  # Convert tuple to string before calling translate
    print(i)
    headerList.append(i)

#print(headerList)

df.to_csv (r'data.csv', header=headerList, index = False) # place 'r' before the path name
df = pd.read_csv('data.csv')
df.to_json(r'data.json', orient='records', lines=True)



