from flask import Flask, jsonify, request, url_for, send_from_directory, render_template, flash, session, redirect, abort
from flask_cors import CORS
import requests
import json
import os
import re
import collections
import datetime

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
        completedFile = baseUserDir + "/completedBOA"
        timeStampsFile = baseUserDir + "/timeStampsBOA"
        open(completedFile, "a")
        open(timeStampsFile, "a")
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
        print "hello" + orderedInput
        comparedOutput = comparePass(orderedInput, allPassword)
        saveSuc = saveDBase(comparedOutput)
        if not saveSuc:
            print "BOA output"
            print comparedOutput
            return jsonify({'result':False, 'error' : "Crash and burn, call moderator"})
        return jsonify({'result':True, 'buttonToggle' : comparedOutput})
    return jsonify({'result':False, 'error' : 'Crash and Burn, call moderator'})

def saveDBase(comparedOutput):
    try:
        currUserScoreFpath = baseUserDir + session['logID'] + "/completedBOA"
        timeStamps = baseUserDir + session['logID'] + "/timeStampsBOA"
        f = open(currUserScoreFpath, "r")
        currCompleted = f.read().split("\n")
        f.close()
        q = open(currUserScoreFpath, "a+")
        y = open(timeStamps, "w")
        newWriteStr = ""
        for i in range(len(comparedOutput)):
            if comparedOutput[i]:
                newWriteStr = "boa" + str(i + 1)
                if newWriteStr not in currCompleted:
                    q.write(newWriteStr+"\n")
                    y.write(str(datetime.datetime.now().time()))
        q.close()
        return True
    except:
        return False

def comparePass(orderedInput, allPassword):
    compareArray = []
    for i in range(len(orderedInput)):
        compareArray.append(orderedInput[i] == allPassword[i])
    print compareArray
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
    currUserScoreFpath = baseUserDir + session['logID'] + "/completedBOA"
    f = open(currUserScoreFpath, "r")
    completedChals = f.read().split("\n")
    f.close()
    completedChalbool = [False,False,False,False,False]

    if 'boa1' in completedChals:
        completedChalbool[0] = True
    if 'boa2' in completedChals:
        completedChalbool[1] = True
    if 'boa3' in completedChals:
        completedChalbool[2] = True
    if 'boa4' in completedChals:
        completedChalbool[3] = True
    if 'boa5' in completedChals:
        completedChalbool[4] = True

    print completedChalbool
    return jsonify({'allChallenges':completedChalbool})

@app.route('/checkSQL', methods = ['POST'])
def checkSQL():
    if not session['logged_in'] or session['logID'] == None:
        return jsonify({'result':False, 'error' : 'Nice Try'})
    if request.method == 'POST':
        sqlPassUserInputob = json.loads(request.data.decode())
        sqlPassUserInput = sqlPassUserInputob['sqlPass']
        if sqlPassUserInput == 'littlebobbytables327':
            saveSQLDB()
            return jsonify({'sqlCompleted' : True})
        else:
            return jsonify({'sqlCompleted' : False})
    return jsonify({'result':False, 'error': "Crash and Burn, or you tried something you were not supposed to"})

def saveSQLDB():
    currUserScoreFpathSQL = baseUserDir + session['logID'] + "/completedSQL"
    currUserScoreFpathSQLTime = baseUserDir + session['logID'] + "/completedSQLTime"
    f = open(currUserScoreFpathSQL, "a+")
    f.write("sqlInj")
    f.close()
    q = open(currUserScoreFpathSQLTime, "a+")
    q.write(str(datetime.datetime.now().time()))
    q.close()

@app.route('/checkSQLDBase', methods = ['GET'])
def checkSQLDbase():
    currUserScoreFpathSQL = baseUserDir + session['logID'] + "/completedSQL"
    f = open(currUserScoreFpathSQL, "r")
    completedFlag = f.read()
    print completedFlag
    f.close()
    if completedFlag != "" or completedFlag != None:
        return jsonify({'sqlCompleted' : True})
    return jsonify({'sqlCompleted' : False})
