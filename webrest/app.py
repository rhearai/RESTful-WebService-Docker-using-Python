from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

chocolate = [
    {
        'id': '1001',
        'name': 'Kitkat',
        'title': 'Wafer',
        'base': 'Biscuit'
    },
    {
        'id': '1002',
        'name': 'Twix',
        'title': 'Bar',
        'base': 'Caramel'
    },
    {
        'id': '1003',
        'name': 'Bounty',
        'title': 'Bar',
        'base': 'Coconut'
    },
    {
        'id': '1004',
        'name': 'M&M',
        'title': 'Small',
        'base': 'Toffee'
    },
    {
        'id': '1005',
        'name': 'Lindt',
        'title': 'Truffle',
        'base': 'Milk'
    },
    {
        'id': '1006',
        'name': 'Ice Breakers',
        'title': 'Small',
        'base': 'Mints'
    },
    {
        'id': '1007',
        'name': 'Orbit',
        'title': 'Small',
        'base': 'Mints'
    },
    {
        'id': '1008',
        'name': 'Ice Breakers',
        'title': 'Small',
        'base': 'Mints'
    },
    {
        'id': '1006',
        'name': 'Kisses',
        'title': 'Small',
        'base': 'Caramel'
    },
    {
        'id': '1007',
        'name': 'Milky way',
        'title': 'Bar',
        'base': 'Caramel'
    },
    {
        'id': '1008',
        'name': 'Crunch',
        'title': 'Bar',
        'base': 'Crispies'
    },
    {
        'id': '1009',
        'name': 'Butterfingers',
        'title': 'Bar',
        'base': 'Peanut'
    },
    {
        'id': '1010',
        'name': 'Reeses',
        'title': 'Cups',
        'base': 'Peanut'
    }
]


@app.route('/chocolate', methods=['GET'])
def getAllChoc():
    return jsonify({'choc': chocDB})


@app.route('/chocolate/<chocId>', methods=['GET'])
def getChocID(chocId):
    usr = [choc['title'] for choc in chocDB if (choc['id'] == chocId)]
    return jsonify({'ID': usr})


@app.route('/chocolate/<chocId>/<choctitle>', methods=['GET'])
def getChocTitle(chocId, choctitle):
    usr = [choc['base'] for choc in chocDB if (choc['id'] == chocId) & ((choc['title'] == choctitle))]
    return jsonify({'Base': usr})


@app.route('/chocolate/<chocId>/<choctitle>/<chocbase>', methods=['GET'])
def getChoc(chocId, choctitle, chocbase):
    usr = [choc for choc in chocDB if
           (choc['id'] == chocId) & ((choc['title'] == choctitle)) & (choc['base'] == chocbase)]
    return jsonify({'choc': usr})


@app.route('/chocolate/<chocID>', methods=['PUT'])
def updateChoc(chocId):
    em = [choc for choc in chocDB if (choc['id'] == chocId)]
    if 'name' in request.json:
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    if 'base' in request.json:
        em[0]['base'] = request.json['base']
        return jsonify({'choc': em[0]})


@app.route('/chocolate', methods=['POST'])
def createChoc():
    dat = {
        'id': request.json['id'],
        'name': request.json['name'],
        'title': request.json['title'],
        'base': request.json['base']
    }
    chocDB.append(dat)
    return jsonify(dat)


@app.route('/chocolate/<chocId>', methods=['DELETE'])
def deleteChoc(chocId):
    em = [choc for choc in chocDB if (choc['id'] == chocId)]
    if len(em) == 0:
        abort(404)
    chocDB.remove(em[0])
    return jsonify({'response': 'Success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
