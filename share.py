import mysql.connector
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

config = configparser.ConfigParser()
config.read('helpers/config.ini')

host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

CEventID = cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
CEventID = cursor.fetchone()[0]

print("Running share.py")

query = "SELECT element FROM share WHERE share = 1"
cursor.execute(query)
elementList = (cursor.fetchall())
elements = str(elementList)
elements = elements.replace(",), (", ", ")
elements = elements.replace(elements[len(elements) - 3:], "")
elements = elements.replace(elements[0],"")
elements = elements.replace(elements[0],"")
elements = elements.translate(str.maketrans("", "", "'"))

query = f"SELECT {elements} FROM matchScouting WHERE eventID = {CEventID}"
cursor.execute(query)
sharedData = cursor.fetchall()
print(sharedData)
df = pd.DataFrame(sharedData)

headerList = []
for i in elementList:
    i = str(i).translate(str.maketrans("", "", "(),"))  # Convert tuple to string before calling translate
    headerList.append(i)

df.to_csv (r'195scoutingData.csv', header=headerList, index = False) # place 'r' before the path name
df = pd.read_csv('195scoutingData.csv')
df.to_json(r'195scoutingData.json', orient='records', lines=True)

print("share.py complete")

cursor.close()
conn.close()
