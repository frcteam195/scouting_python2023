import sqlite3

# connect to the database
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# create the matchComparison table
c.execute('''CREATE TABLE matchComparison
             (team text, eventID text, matchNum integer, red1 text, red2 text, red3 text,
             blue1 text, blue2 text, blue3 text, redAutoScore integer, redTeleScore integer,
             redCSpts integer, blueAutoScore integer, blueTeleScore integer, blueCSpts integer,
             totalRedAutoScore integer, totalRedTeleScore integer, totalRedCSpts integer,
             totalBlueAutoScore integer, totalBlueTeleScore integer, totalBlueCSpts integer)''')

# iterate over the matches table
for row in c.execute('SELECT * FROM matches'):
    matchID, eventID, matchNum, red1, red2, red3, blue1, blue2, blue3, redAutoScore, redTeleScore, redCSpts, blueAutoScore, blueTeleScore, blueCSpts = row

    # sum the results for the red alliance
    totalRedAutoScore = 0
    totalRedTeleScore = 0
    totalRedCSpts = 0
    for team in [red1, red2, red3]:
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=4 AND team='{}'".format(matchNum, team)):
            totalRedAutoScore += r[0]
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=6 AND team='{}'".format(matchNum, team)):
            totalRedTeleScore += r[0]
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=9 AND team='{}'".format(matchNum, team)):
            totalRedCSpts += r[0]

    # sum the results for the blue alliance
    totalBlueAutoScore = 0
    totalBlueTeleScore = 0
    totalBlueCSpts = 0
    for team in [blue1, blue2, blue3]:
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=4 AND team='{}'".format(matchNum, team)):
            totalBlueAutoScore += r[0]
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=6 AND team='{}'".format(matchNum, team)):
            totalBlueTeleScore += r[0]
        for r in c.execute("SELECT M{} FROM CEanalysis WHERE analysisTypeID=9 AND team='{}'".format(matchNum, team)):
            totalBlueCSpts += r[0]

    # insert the data into the matchComparison table
    c.execute('''INSERT INTO matchComparison
                 (team, eventID, matchNum, red1, red2, red3, blue1, blue2, blue3, redAutoScore, redTeleScore,
                 redCSpts, blueAutoScore, blueTeleScore, blueCSpts, totalRedAutoScore, totalRedTeleScore,
                 totalRedCSpts, totalBlueAutoScore, totalBlueTeleScore, totalBlueCSpts)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (None, eventID, matchNum, red1, red2, red3, blue1, blue2, blue3, redAutoScore, redTeleScore,
               redCSpts, blueAutoScore, blueTeleScore, blueCSpts, total




