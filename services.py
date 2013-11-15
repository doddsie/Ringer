__author__ = 'ddodd'


from flask import Flask, jsonify


from ringerfinder import getRingers

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"




@app.route('/hockey/ringers/v1.0/list', methods = ['GET'])
def get_ringers():
    ringers = getRingers(25, 3.0)



    for ringer in ringers:
        if (ringer.leveldiff > 3):
            #print "Ringer: %s leveldiff %s" % (ringer.name,  ringer.leveldiff)
            for player in ringer.players:
                playerDivision = divisions[player.divisionId]
                playerTeam = teams[player.teamId]



                #printRinger(playerDivision, playerTeam, player)



    return jsonify( { 'ringers': ringers } )






if __name__ == '__main__':
    app.run(debug = True)