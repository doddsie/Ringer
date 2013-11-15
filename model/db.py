__author__ = 'ddodd'

import sqlite3
import os

dbFile = 'hockey.db'
conn = None

def dropDb():
    try:
        db = open(dbFile, "r")
        db.close()
        os.remove(dbFile)
    except IOError:
        return

def _getConnection():
    global conn

    if conn == None:
        conn = sqlite3.connect('hockey.db')

    return conn

def closeConnection():
    if conn != None:
        conn.commit()
        conn.close()

def getCursor():
    return _getConnection().cursor()

def createTables():
    cursor = getCursor()
    cursor.execute('''CREATE TABLE season (seasonId INTEGER, name TEXT) ''')
    cursor.execute('''CREATE TABLE division (seasonId INTEGER, divisionId INTEGER, divisionName TEXT, divisionLevel INTEGER) ''')
    cursor.execute('''CREATE TABLE team (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, teamName TEXT, divisionUrl TEXT) ''')
    cursor.execute('''CREATE TABLE player
    (seasonId INTEGER,  divisionId INTEGER, teamId INTEGER, name TEXT, firstname TEXT, lastname TEXT, middleName TEXT, number TEXT, gamesPlayed INTEGER, goals INTEGER, assists INTEGER, points INTEGER, average FLOAT) ''')
    cursor.connection.commit()
    cursor.close()

def removeSeason(seasonId):
    cursor = getCursor()
    cursor.execute('DELETE from season where seasonId=' + str(seasonId))
    cursor.execute('DELETE from division where seasonId=' + str(seasonId))
    cursor.execute('DELETE from team where seasonId=' + str(seasonId))
    cursor.execute('DELETE from player where seasonId=' + str(seasonId))
    cursor.close()


'''

                   #print td
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
                    newPlayer.stats = float(float(newPlayer.points) / float(newPlayer.gamesPlayed))

'''''