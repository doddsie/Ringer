__author__ = 'ddodd'

import unittest
import urllib2

from bs4 import BeautifulSoup  # For processing HTML


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


        sampleTeamUrl = 'file:///Users/ddodd/PycharmProjects/RingerFinder/test/sampleTeam'


        data = urllib2.urlopen('file:///Users/ddodd/PycharmProjects/RingerFinder/test/sampleLeague')
        soup = BeautifulSoup(data.read())



if __name__ == '__main__':
    unittest.main()
