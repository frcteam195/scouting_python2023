print()
print("Looping through matchScouting and matchScoutingL2, comparing teams to the matches table and")
print("fixing any team numbers that are incorrect. Helpful if schedule was hand built initially")
print()

tables = ['matchScouting', 'matchScoutingL2']

dict = {1: {'allianceStationID': 1, 'allianceStation': 'red1'},
         2: {'allianceStationID': 2, 'allianceStation': 'red2'},
         3: {'allianceStationID': 3, 'allianceStation': 'red3'},
         4: {'allianceStationID': 4, 'allianceStation': 'blue1'},
         5: {'allianceStationID': 5, 'allianceStation': 'blue2'},
         6: {'allianceStationID': 6, 'allianceStation': 'blue3'}}
# print(dict)

for table in tables:
    
    j = 1
    while j <= 6:
        allianceStationID = dict[j]['allianceStationID']
        allianceStation = dict[j]['allianceStation']
        # print(f"{allianceStationID} {allianceStation}")
        print(f"{table}:  fixing team # typos for allianceStation {allianceStation}")
        updateQuery = "UPDATE " + table + " INNER JOIN matches ON (" + table + ".matchID = matches.matchID) " + \
                "INNER JOIN events ON (events.eventID = matches.eventID) " + \
                "SET " + table + ".team = matches." +  allianceStation + " " + \
                "WHERE events.currentEvent = 1 AND " + table + ".allianceStationID = " + str(allianceStationID) + ";"
        cursor.execute(updateQuery)
        conn.commit()
        j += 1