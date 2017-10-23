from flask_login import UserMixin
import csv

def read(csv_file):
    items = []
    with open(csv_file,'r') as csv_in:
        reader = csv.reader(csv_in)
        for row in reader:
            items.append(row)
    return items

def read_courses(csv_file):
    items = []
    with open(csv_file, 'r') as csv_in:
        reader = csv.reader(csv_in)
        for column in reader:
            items.append(column[1])
    return items

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Student:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Staff:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class User(UserMixin):
    def __init__(self, userID):
        self.userID = userID
        self.username = username
        self.password = password

    @classmethod
    def search_user(self, username, password):
       with open('passwords.csv', 'rt') as f:
          #reader = csv.reader(f, delimiter=',')
          reader = read('passwords.csv')
          for column in reader:
             print(column)
             if username == column[1] and password == column[2]: # if the username shall be on column 3 (-> index 2)
                print "Logging in..."
                return True

    @classmethod
    def create_user(self, new_row):
       # Writes userID to respondents.csv
       with open('respondents.csv','a') as csv_out:
          writer = csv.writer(csv_out)
          writer.writerow(new_row)

class Survey(object):
    def __init__(self, surveyID, surveyName, course):
        self.surveyID = surveyID
        self.surveyName = surveyName
        self.course = course
        self.questions = []
        self.responses = []

    @classmethod
    def add_question(self, question):
        self.questions.append(question)

    @classmethod
    def add_response(self, response):
        self.responses.append(response)

    @classmethod
    def create_survey(self, surveyName, newSurvey):
       # Creates new csv file using selected questions and inputted name
       with open(str(surveyName) + '.csv','a') as csv_make:
          writer = csv.writer(csv_make)
          writer.writerow(newSurvey)

class Question:
    def __init__(self, questionId, title):
        self.quesitonId = questionId
        self.title = title

    @classmethod
    def create_question(self, question):
       with open('questions.csv','a') as csv_out:
          writer = csv.writer(csv_out)
          writer.writerow(question)

class MultQuestion(Question):
    def __init__(self, questionId, title, options):
        Question.__init__(self, questionId, title)
        self.options = options

class Response:
    def __init__(self, responseId, studentId, questionId, answer):
        self.responseId = responseId
        self.studentId = studentId
        self.questionId = questionId
        self.answer = answer

class Course:
    def __init__(self, courseId, title, semester):
        self.courseId = courseId
        self.title = title
        self.semester = semester
