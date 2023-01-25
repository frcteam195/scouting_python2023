tables = ['matchScouting', 'matchScoutingL2']
for table in tables:
    query = "SELECT " + table + ".id FROM " + table + " INNER JOIN events " + \
            "ON " + table + ".eventID = events.id AND ((events.currentEvent) = 1) " + \
            "WHERE " + table + ".team = " + table + " ORDER BY " + table + ".id;"
    print(query)