__author__ = 'ddodd'


'''
Created on Oct 9, 2013

@author: ddodd
'''
import sys
import os


#COMMON KLUDGE
#to allo our script to be invokded from anywhwere

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, "src"))
from ringerfinder import getRingers
from ringerfinder import getTeams
from ringerfinder import getDivisions
from ringerfinder import getSeasons


from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/")
def home():

    ringers = getRingers(25, 2.00)
    teams = getTeams(25)
    divisions = getDivisions(25)
    seasons = getSeasons()
    output = ""

    data  = {}
    data["ringers"] = ringers
    data["teams"] = teams
    data["divisions"] = divisions
    data["seasons"] = seasons

#    for ringer in ringers:
#        output += "<li>" + ringer.name + "</li>";

    return  render_template("index.html", **data)

if __name__ == '__main__':
    app.run(port=5555, debug=True)