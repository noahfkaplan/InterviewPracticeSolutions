import os
import re

class QuestionService():
    def getQuestionList():
        os.chdir("DailySolutions")
        years = os.listdir(os.getcwd())
        dates = []
        for year in years:
            os.chdir(year)
            directories = os.listdir(os.getcwd())
            for directory in directories:
                dates.append(directory)
            os.chdir("..")
        os.chdir("..")
        return dates

    def getQuestionByDate(date):
        parsedDate = date.split("-")
        os.chdir("DailySolutions/"+parsedDate[2]+"/"+date)
        questionFile = open("question.txt", "r")
        question = questionFile.read()
        questionFile.close()
        os.chdir("../../..")
        return question

    def getSolutionByDate(date):
        parsedDate = date.split("-")
        solution = ""
        os.chdir("DailySolutions/"+parsedDate[2]+"/"+date)
        files = os.listdir(os.getcwd())
        for file in files:
            if re.match("^.*\.py", file) and not re.match("^.*Tests\.py", file) and not re.match("main.py", file):
                solutionFile = open(file, "r")
                solution = solutionFile.read() + "\n " + solution
                solutionFile.close()
        os.chdir("../../..")
        return solution
    