import mysql.connector
import argparse
import configparser

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
parser.add_argument("-table", "--table", help= "Select the database table name", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host
table_name = args.table

config = configparser.ConfigParser()
config.read('helpers/config.ini')

host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

query = f"SELECT * FROM {table_name} WHERE eventID = 8"
cursor.execute(query)
tableData = cursor.fetchall()

print(tableData)

cursor.close()
conn.close()
