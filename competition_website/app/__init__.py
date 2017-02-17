from flask import Flask, jsonify, request, url_for, send_from_directory, render_template, flash, session, redirect, abort
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def loadIndex():
    return render_template('index.html')
