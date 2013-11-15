__author__ = 'ddodd'

import urllib2

from bs4 import BeautifulSoup  # For processing HTML
from model.season import Season
from model.division import Division
from model.team import Team
from parser.team import parseTeam

baseUrl = 'http://stats.liahl.org/'

def parseSeason(name, seasonUrl):

    data = urllib2.urlopen(seasonUrl)
    soup = BeautifulSoup(data.read())
    teams = []
    divisions  = []
    divisionSet = set()
    currentDivision = None
    divisionLevels = dict()

    seasonId = None
    divisionLevel = 1
    season = Season()
    season.name = name
    season.url = seasonUrl

    teamId = 1
    divisionId = 1

    for link in soup.find_all('a'):
        hrefVal = link.get('href')
        if hrefVal and hrefVal.startswith('display-schedule.php'):
            #print 'Team name is: ' + link.string + ' : ' + hrefVal
            if seasonId is None:
                seasonId = getSeason(hrefVal)
            team = Team()
            team.url = hrefVal
            team.name = link.string
            team.teamId = teamId
            teamId += 1
            team.players = parseTeam(baseUrl + hrefVal)
            if (currentDivision) :
                currentDivision.teams.append(team)

        elif not hrefVal :

            test = link.string.split()
            division = test[1]
            #print 'Division: ' + division

            # Only process
            if division not in divisionSet:
                divisionSet.add(division)
                divisions.append(division)
                divisionLevels[division] = divisionLevel
                divisionLevel += 1

            currentDivision = Division()
            currentDivision.level = divisionLevel
            divisionId += 1
            currentDivision.divisionId =divisionId
            currentDivision.name = link.string

            season.divisions.append(currentDivision )

    season.seasonId = seasonId
    return season


def getSeason(href):
    split = href.split("&")
    for attr in split:
        #print attr
        if attr.startswith("season="):
            season = attr[len("season="):]
            break
    if season:
        #do nothing
        i=0
    else:
        season = "-1"
    return season








