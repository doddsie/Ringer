__author__ = 'ddodd'

import urllib2

from bs4 import BeautifulSoup  # For processing HTML
from model.player import Player


def parseTeam(teamUrl):

    data = urllib2.urlopen(teamUrl)
    soup = BeautifulSoup(data.read())
    players = []

    # List of all td's in order for team players
    # print soup.find_all('a')
    #
    # 0 Name
    # #
    # 2 GP
    # 3 Goals
    # 4 Ass.
    # 5 PPG
    # 6 PPA
    # 7 SHG
    # 8 SHA
    # 9 GWG
    # 10 GWA
    # 11 PSG
    # 12 ENG
    # 13 SOG
    # 14 Pts

    for tr in soup.find_all('tr'):
        if tr and tr.td and tr.td.get('align'):
            tds = tr.find_all('td')

            # Only get the player stats
            if len(tds) == 15 :

                #print len(tds)
                #print(tds)
                #print( type(tds))

                newPlayer = Player()

                #assert isinstance(newPlayer, Player)
                i = 0
                for td in tds:
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
                    newPlayer.average = float(float(newPlayer.points) / float(newPlayer.gamesPlayed))
                else :
                    newPlayer.average = float(0.0)

                players.append(newPlayer)

    return players


#http://stats.liahl.org/display-schedule.php?team=297&season=27&tlev=0&tseq=0&league=1
#'file:///Users/ddodd/PycharmProjects/RingerFinder/parser/sampleteam'
#parseTeam('http://stats.liahl.org/display-schedule.php?team=443&season=25&tlev=0&tseq=0&league=1')
