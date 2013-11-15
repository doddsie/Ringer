__author__ = 'ddodd'


import parser.SeasonParser
import model.db


def enter_season(season):
    print "Season: %s : %s" % ( season.name, season.seasonId )


    insertStmnt = "INSERT INTO season VALUES (%s, '%s')" % (season.seasonId, season.name)
    cursor.execute(insertStmnt)
    for division in season.divisions:
        print "Division %s DivisionId %s DivisionLevel %s" % (  division.name, division.divisionId, division.level )
        insertStmnt = "INSERT INTO division VALUES (%s, %s, '%s', %s)" % (season.seasonId, division.divisionId, division.name, division.level )
        cursor.execute(insertStmnt)

        for team in division.teams:
            print "\tTeam: %s TeamId: %s Url: %s" %( team.name, team.teamId, team.url)
            insertStmnt = "INSERT INTO team VALUES (%s, %s, %s, '%s', '%s')" % (season.seasonId, division.divisionId, team.teamId, team.name, team.url )
            cursor.execute(insertStmnt)
            for player in team.players:
                names = player.name.split()
                if len(names) == 1:
                    firstname = names[0]
                    lastname = ""
                    middle = ""
                    print player.name
                elif len(names) == 2:
                    firstname = names[0]
                    lastname = names[1]
                    middle = ""
                elif len(names) == 3:
                    firstname = names[0]
                    lastname = names[2]
                    middle = names[1]
                    print player.name
                else:
                    firstname = names[0]
                    lastname = names[2]
                    middle = " ".join(names[1:len(names)-1])
                    print player.name


                insertStmnt = "INSERT INTO player VALUES (%s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (season.seasonId, division.divisionId, team.teamId, player.name, firstname, lastname, middle, player.number, player.gamesPlayed, player.goals, player.assists, player.points, player.average )
                cursor.execute(insertStmnt)

    cursor.close()



if __name__ == '__main__':


    model.db.dropDb()
    model.db.createTables()
    cursor = model.db.getCursor()


#    season = parser.SeasonParser.parseSeason("Winter 2012-2013" , "file:///Users/ddodd/PycharmProjects/RingerFinder/test/sampleLeague")
    season = parser.SeasonParser.parseSeason("Winter 2013-2014" , "http://stats.liahl.org/display-stats.php?league=1")
#http://stats.liahl.org/display-stats.php?league=1

    enter_season(season)

    season = parser.SeasonParser.parseSeason("Winter 2012-2013" , "http://stats.liahl.org/display-stats.php?league=1&season=25")
    enter_season(season)


    cursor.close()

    model.db.closeConnection()



"""

   cursor.execute('''CREATE TABLE player
    (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, name TEXT, firstname TEXT, lastname TEXT, middleName TEXT, number TEXT, gamesPlayed INTEGER, goals INTEGER, assists INTEGER, points INTEGER, averagePoints FLOAT) ''')

       if i==0:
            newPlayer.name = td.string
        elif i == 1:
            newPlayer.number = td.string
        elif i == 2:
            newPlayer.gamesPlayed = td.string
        elif i == 3:
            newPlayer.goals = td.string
        elif i == 4 :
            newPlayer.assists = td.string
        elif i == 14 :
            newPlayer.points = td.string
        i = i + 1

    if int(newPlayer.gamesPlayed) != 0 :
        newPlayer.average = float(float(newPlayer.points) / float(newPlayer.gamesPlayed))
    else :
        newPlayer.average = float(0.0)

    players.append(newPlayer)



    cursor.execute('''CREATE TABLE season (seasonId INTEGER, name TEXT) ''')
    cursor.execute('''CREATE TABLE division (seasonId INTEGER, divisionId INTEGER, divisionName TEXT, divisionLevel INTEGER) ''')
    cursor.execute('''CREATE TABLE team (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, teamName TEXT, divisionUrl TEXT) ''')





# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

team = Team()
team.url = hrefVal
team.name = link.string
team.teamId = teamId


currentDivision.level = divisionLevel
divisionId += 1
currentDivision.divisionId =divisionId
currentDivision.name = link.string

"""