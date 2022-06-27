import helpers.dbLogin as db
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: aws-prod, aws-dev", required= True)
args = parser.parse_args()
input_database = args.database

db.login(input_database)

print(db.getdict())
