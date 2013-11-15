__author__ = 'ddodd'


from model.season import Season
import urllib2

#def test():

  #  season = Season()

 ##   season.name = "test"



                #print(type(newPlayer.name))
               # if newPlayer.stats :
                    #print

                #    hrefVal = link.get('href')
                #   if hrefVal and hrefVal.startswith('display-schedule.php'):
                #      print 'Team name is: ' + link.string + ' : ' + hrefVal
                #   elif not hrefVal :
                #     print 'Division: ' + link.string
 #   data = urllib2.urlopen(url)
  #  print data.read()
  #  f = open('league','r')

   #print soup.prettify()

   # print soup.find_all('a')

#parseSeason("http://stats.liahl.org/display-stats.php?league=1")
#readSeason("http://stats.liahl.org/display-stats.php?league=1")
#getSampleTeam()


def getSampleTeam():
    data = urllib2.urlopen('http://stats.liahl.org/display-schedule.php?team=443&season=25&tlev=0&tseq=0&league=1')
    f = open('sampleteam', 'w')
    f.write(data.read())
    f.close()

def readSeason(url):
    data = urllib2.urlopen(url)
    f = open('league', 'w')
    f.write(data.read())
    f.close()


class T1(object):
    def __init__(self):
        self.id = 123
    name="test"

str = "This is my dog"
split = str.split()
print split[1:len(split)-1]

