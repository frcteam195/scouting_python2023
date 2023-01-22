# Python3 script that pulls all FRC registered teams for the current year and
#	writes the full team list to the Teams table in the Team 195 DB
# Script is intended to be run once at the beginning of the season

import mariadb as mariaDB
import tbapy
import datetime
import sys
import argparse
import configparser

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

# Read the configuration file
config = configparser.ConfigParser()
config.read('../helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)

conn = mariaDB.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

tba = tbapy.TBA('Tfr7kbOvWrw0kpnVp5OjeY780ANkzVMyQBZ23xiITUkFo9hWqzOuZVlL3Uy6mLrz')
#currentYear = datetime.datetime.today().year
currentYear = 2022

def wipeTTL():
        cursor.execute("DELETE FROM teamsAll;")
        cursor.execute("ALTER TABLE teamsAll AUTO_INCREMENT = 1;")
        conn.commit()

wipeTTL()

def onlyascii(s):
    return "".join(i for i in s if ord(i) < 128 and ord(i) != 39)


totalTeams = tba.teams(year=currentYear)
teamList = []

for team in totalTeams:
    
    tempNick = ''
    tempLocation = ''
    tempCity = ''
    tempStateProv = ''
    tempCountry = ''
    
    teamNum = team.get('team_number')
    location = str(team.city) + ' ' + str(team.state_prov) + ' ' + str(team.country)    
    
    tempNick = onlyascii(team.nickname)
    tempLocation = onlyascii(location)
    tempCity = onlyascii(team.city)
    tempStateProv = onlyascii(team.state_prov)
    tempCountry = onlyascii(team.country)
    
    if len(tempNick) > 50:
        tempNick = tempNick[:40]
    if len(tempLocation) > 50:
        tempLocation = tempLocation[:40]
    if len(tempCity) > 50:
        tempCity = tempCity[:40]
    if len(tempStateProv) > 50:
        tempStateProv = tempStateProv[:40]
    if len(tempCountry) > 50:
        tempCountry = tempCountry[:40]
    
    query = "INSERT INTO teamsAll (team, teamName, teamLocation, teamCity, teamStateProv, teamCountry) VALUES " + \
            "('" + str(teamNum) + \
            "','" + str(tempNick) + \
            "','" + str(tempLocation) + \
            "','" + str(tempCity) + \
            "','" + str(tempStateProv) + \
            "','" + str(tempCountry) + "');"
    print(query)
    
    cursor.execute(query)
    conn.commit()