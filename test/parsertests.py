__author__ = 'ddodd'

import unittest
import urllib2

from parser.season import parseSeason
from parser.team import  parseTeam

from bs4 import BeautifulSoup  # For processing HTML


class TestTeamParser(unittest.TestCase):
    def testTeamParser(self):
        peeps = parseTeam('file:///Users/ddodd/PycharmProjects/RingerFinder/test/sampleTeam')
        for player in peeps :
             print player.number + " : " +  player.name + " : " + player.points + " : " +  str(player.average)

        print(" count : " + str(len(peeps)))
        self.assertEqual(True, True)
        self.assertEqual(28, len(peeps))


class TestLeagueParser(unittest.TestCase):
    def testLeagueParser(self):
 #       teams = parseSeason('file:///Users/ddodd/PycharmProjects/RingerFinder/test/sampleLeague')
        pass

class TestSeasonParser(unittest.TestCase):
    def testSeasonParser(self):


        html =  "<a href=\"display-schedule.php?team=43&amp;season=27&amp;tlev=0&amp;tseq=0&amp;league=1\">"

        soup = BeautifulSoup(html)
        link = soup.find("a")
        href = link.hrefVal = link.get('href')
        split = href.split("&")
        for attr in split:
            print attr
            if attr.startswith("season="):
                season = attr[len("season="):]
                break
        if season:
            print season

        self.assertEqual(27, int(season))


if __name__ == '__main__':
    unittest.main()
