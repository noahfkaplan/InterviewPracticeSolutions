from flask import Flask, request, jsonify, Blueprint
from WebApi.QuestionService import QuestionService
import json

question_api = Blueprint("question_api", __name__)

@question_api.route("/questions")
def questionList():
    result = QuestionService.getQuestionList()
    return jsonify({"questions": result})
