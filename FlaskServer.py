
import json
from flask import Flask, request
from tools.other import Time
from tools.db import DbHelper

app = Flask(__name__)
@app.route('/userInfo')
def getUserInfo():
    userId = request.args.get('userId')
    return json.dumps({'info': DbHelper.getUserInfo(userId)})

#Return most up to date net worth
@app.route('/getUserNetWorth')
def getUserInfo():
    userId = request.args.get('userId')
    return json.dumps({'info': DbHelper.getUserInfo(userId)})


app.run(port=5001)