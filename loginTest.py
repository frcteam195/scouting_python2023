#import configparser
import dbLogin as p
import argparse
import sys
#c = configparser.ConfigParser()

parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: aws-prod, aws-dev", required= True)
args = parser.parse_args()
input_database = args.database

p.login(input_database)


print(p.getdict())
