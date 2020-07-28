
import json
from flask import Flask, request
from tools.db.helpers import DbHelper

app = Flask(__name__)
@app.route('/userInfo')
def getUserInfo():
    userId = request.args.get('userId')
    return json.dumps({'info': DbHelper.getUserInfo(userId)})

#Return most up to date net worth
@app.route('/getUserNetWorth')
def getUserNetWorth():
    userId = request.args.get('userId')
    return json.dumps({'info': DbHelper.getUserInfo(userId)})


app.run(port=5001)