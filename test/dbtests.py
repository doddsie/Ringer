__author__ = 'ddodd'


import unittest
#import model.db as db
from model import db

class DBTests(unittest.TestCase):
    def testCreateDb(self):

        """


        """
        self.assertEqual(True, True)
        print('test one')

       # db.dropDb()
        #db.createTables()
        db.closeConnection()

    def testShowRows(self):
        cursor = db.getCursor()

        #db.removeSeason(27)
        # Print the table contents
        for row in cursor.execute("select *  from season where seasonId=25"):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from division where seasonId=25"):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from team where seasonId=25"):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from player where seasonId=25"):
            print row

        cursor.close()
        db.closeConnection()

    def testShowRows(self):
        cursor = db.getCursor()

        #db.removeSeason(27)
        # Print the table contents
        for row in cursor.execute("select *  from season"):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from division"):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from team "):
            print row

        # Print the table contents
        for row in cursor.execute("select *  from player "):
            print row

        cursor.close()
        db.closeConnection()


if __name__ == '__main__':
    unittest.main()