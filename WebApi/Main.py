from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from QuestionAPI import question_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(question_api)