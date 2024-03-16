from flask import Flask, request

app = Flask(__name__)

@app.route('/cry', methods=['GET'])
def cryALot():
    amCry = request.args.get('answer', '').lower()
    if amCry == 'yes':
        return 'You are Sailor Moon!'
    else:
        return 'Guess you\'re not Sailor Moon then'

@app.route('/smart', methods=['GET'])
def smart():
    amSmart = request.args.get('answer', '').lower()
    if amSmart == 'yes':
        return 'You are Sailor Mercury!'
    else:
        return 'Welp, not Sailor Mercury either'

@app.route('/strong', methods=['GET'])
def strong():
    amStrong = request.args.get('answer', '').lower()
    if amStrong == 'yes':
        return 'You are Sailor Jupiter!'
    else:
        return 'Not Sailor Jupiter either'

@app.route('/cool', methods=['GET'])
def cool():
    amCool = request.args.get('answer', '').lower()
    if amCool == 'yes':
        return 'You are Sailor Mars!'
    else:
        return 'Okay so you aren\'t Sailor Mars either then'

@app.route('/pretty', methods=['GET'])
def pretty():
    amPretty = request.args.get('answer', '').lower()
    if amPretty == 'yes':
        return 'You are Sailor Venus!'
    else:
        return 'Aww, guess you aren\'t like any of the Sailor Scouts then'

if __name__ == '__main__':
    app.run(debug=True)