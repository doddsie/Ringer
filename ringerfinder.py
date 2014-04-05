

from model.division import Division
from model.team import Team
from model.player import Player
from model.season import Season
from model import db

def createPlayer(row):
    player = Player()
    player.divisionId = row[1]
    player.teamId = row[2]
    player.name = row[3]
    player.gamesPlayed = row[8]
    player.goals = row[9]
    player.assists = row[10]
    player.points = row[11]
    player.average = row[12]

    return player


def printRinger(playerDivision, playerTeam, player):
    print "\tplaying on team %s in division %s level %s %s" % (playerTeam.name,  playerDivision.name, playerDivision.level, player.average)



uniqueRingers = {}
divisions = {}
teams = {}
players = []
seasons = {}


def ringerFilter(ringer) :
    if ringer.name not in uniqueRingers:
        uniqueRingers[ringer.name]  = True
        return True
    else:
        return False

def playerSortByDivision(player):
    division = divisions[player.divisionId]
    return division.level



def getSeasons():

    cursor = db.getCursor()
    for row in cursor.execute("select *  from season"):
        season = Season()
        season.id = row[0]
        season.name = row[1]

        seasons[row[0]] = season



def getDivisions(seasonId):
    cursor = db.getCursor()

    # Print the table contents

 #   cursor.execute('''CREATE TABLE division (seasonId INTEGER, divisionId INTEGER, divisionName TEXT, divisionLevel INTEGER) ''')
    for row in cursor.execute("select *  from division where seasonId=" + str(seasonId)):
        division = Division()
        division.divisionId = row[1]
        division.name = row[2]
        division.level = row[3]
        divisions[row[1]] = division

    return divisions


def getTeams(seasonId):
    cursor = db.getCursor()

    # Print the table contents
#    cursor.execute('''CREATE TABLE team (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, teamName TEXT, divisionUrl TEXT) ''')
    for row in cursor.execute("select *  from team where seasonId=" +  str(seasonId)):
        team = Team()
        team.divisionId = row[1]
        team.teamId = row[2]
        team.name = row[3]
        teams[row[2]] = team

    return teams



def getRingers(seasonId, minAverage):
    global uniqueRingers
    cursor = db.getCursor()

    teams = getTeams(seasonId)
    divisions = getDivisions(seasonId)

#    cursor.execute('''CREATE TABLE player
#    (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, name TEXT, firstname TEXT, lastname TEXT, middleName TEXT, number TEXT, gamesPlayed INTEGER, goals INTEGER, assists INTEGER, points INTEGER, average FLOAT) ''')
    # Print the table contents
    for row in cursor.execute("select *  from player where seasonId=" +  str(seasonId)):
        player = createPlayer(row)
        players.append(player)

    ringers = []

    select = "select *  from player where seasonId=%s and average>%s" % (seasonId, minAverage)
    for row in cursor.execute(select):
        player = createPlayer(row)
        division = divisions[player.divisionId]

        # Filter out players that are playing a really high level already... who cares... :)
        if (division.level > 4):
            ringers.append(player)

    cursor.close()


    uniqueRingers = {}

    #Filter out the duplicates
    ringers = filter(ringerFilter, ringers)


    for ringer in ringers:
        # Look for the ringer in all the players, see if they play in any other league
        ringer.players = []

        found = False
        for player in players:

            if player.name == ringer.name and player.teamId != ringer.teamId:
                ringerTeam = teams[ringer.teamId]
                if not found:
                    found = True
                    ringerDivision = divisions[ringer.divisionId]
                    ringer.players.append(ringer)
                   # print "Ringer: %s playing on team %s in division %s level %s %s" % (ringer.name, ringerTeam.name, ringerDivision.name, ringerDivision.level, ringer.average)

                # we have a ringer!!!!!
                playerTeam = teams[player.teamId]
                playerDivision = divisions[player.divisionId]
                ringer.players.append(player)
                #printRinger(playerDivision, playerTeam,  player)

    for ringer in ringers:
        ringer.players = sorted(ringer.players,
                      key=playerSortByDivision,
                     reverse=True)

        if len(ringer.players):
            baseLevelDivision  = divisions[ringer.players[0].divisionId]
            maxLevelDivsion = divisions[ringer.players[len(ringer.players)-1].divisionId]
            ringer.leveldiff = baseLevelDivision.level - maxLevelDivsion.level
        else:
            ringer.leveldiff = 0

    return ringers

if __name__ == '__main__':
    ringers = getRingers(27, 1.75)
    for ringer in ringers:
        if (ringer.leveldiff > 3):
            print "Ringer: %s leveldiff %s" % (ringer.name,  ringer.leveldiff)
            for player in ringer.players:
                playerDivision = divisions[player.divisionId]
                playerTeam = teams[player.teamId]
                printRinger(playerDivision, playerTeam, player)
