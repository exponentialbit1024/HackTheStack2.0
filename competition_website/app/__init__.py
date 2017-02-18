from flask import Flask, jsonify, request, url_for, send_from_directory, render_template, flash, session, redirect, abort
from flask_cors import CORS
import requests
import json
import os
import re
import collections

app = Flask(__name__)
CORS(app)
app.secret_key = 'hackTStack2ieeecsocietypurdue'

baseUserDir = "../../../userScores/"

@app.route('/')
def loadIndex():
    try:
        uid = session['logID']
        logged_inFlag = session['logged_in']
        return render_template('challenges.html', lusername=uid)
    except:
        session.pop('logID', None)
        session.pop('logged_in', False)
        return render_template('index.html')

@app.route('/loginAuth', methods = ['POST'])
def checkLogin():
    if request.method == 'POST':
        loginData = json.loads(request.data.decode())
        loginID = loginData['logID']
        checkBadLogin = checkValidString(loginID)
        if not checkBadLogin:
            return jsonify({'result':False,'error':'Nice try Injections will not work here'})
        loginResult = checkUserExists(loginID)
        newUserSuccess = True
        if not loginResult:
            newUserSuccess = createNewUser(loginID)
        if not newUserSuccess:
            return jsonify({'result':newUserSuccess,'errors':'Directory not created'})
        session['logID'] = loginID
        session['logged_in'] = True
        return jsonify({'result':True})
    else:
        return jsonify({'result' : 'Either you tried something you were not supposed to, or something broke'})
    return jsonify({'result':'Nice Try'})

def checkValidString(inp):
	if re.match("^[A-Za-z0-9_-]*$", inp):
		return True
	else:
		return False

def checkUserExists(loginID):
    userScoreDirs = baseUserDir
    currUsers = list(os.listdir(userScoreDirs))
    print currUsers
    if loginID in currUsers:
        return True
    return False

def createNewUser(loginID):
    try:
        newDirPath = baseUserDir + loginID
        os.makedirs(newDirPath)
        return True
    except:
        return False

@app.route('/logout')
def logoutUser():
    session.pop('logID', None)
    session.pop('logged_in', False)
    return redirect('/')

@app.route('/faq')
def loadFaq():
    return render_template('faq.html')

@app.route('/checkBOA', methods = ['POST'])
def checkBOAPass():
    if not session['logged_in'] or session['logID'] == None:
        return jsonify({'result':False, 'error' : 'Nice Try'})
    if request.method == 'POST':
        getAllPostedPasswords = json.loads(request.data.decode())
        if len(getAllPostedPasswords) == 0:
            return jsonify({'result':False, 'error':'You need real passwords, we have a real comparator.'})
        orderedInput = orderUserInputBOAPass(getAllPostedPasswords)
        allPassword = getPasswords()
        if allPassword == None:
            return jsonify({'result': 'Crash and Burn, call moderator, there might be an issue with retriving comparator passwords.'})
        comparedOutput = comparePass(orderedInput, allPassword)
        return jsonify({'result':True, 'buttonToggle' : comparedOutput})
    return jsonify({'result':False, 'error' : 'Crash and Burn, call moderator'})

def comparePass(orderedInput, allPassword):
    compareArray = []
    for i in range(len(orderedInput)):
        compareArray.append(orderedInput[i] == allPassword[i])
    return compareArray

def orderUserInputBOAPass(userInputBOADict):
    od = collections.OrderedDict(sorted(userInputBOADict.items()))
    boaOrderedArray = []
    for key, value in od.iteritems():
        boaOrderedArray.append(value)
    return boaOrderedArray

def getPasswords():
    try:
        f = open("./app/challengePassKeys", "r")
        allPass = f.read().split("\n")
        allPass.pop(len(allPass) - 1)
        justPasses = []
        for i in range(len(allPass)):
            justPasses.append(allPass[i].split("=")[1])
        return justPasses
    except:
        return None

@app.route('/getBOADBase', methods = ['GET'])
def checkDBaseBOA():
    if not session['logged_in'] or session['logID'] == None:
        return jsonify({'result':False, 'error' : 'Nice Try'})
    currUserScoreFpath = baseUserDir + session['logID'] + "/completed"
    
    return False
