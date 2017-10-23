from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Question, Response, Answer, Survey

class App(object):
    def addQuestion(self, id, title, type, surveyId):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        newQuestion = Question(id=id, title=title, type=type, surveyId=surveyId)
        session.add(newQuestion)
        session.commit()
        session.close()

    def addResponse(self, id, studentId, surveyId):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        newResponse = Response(id=id, studentId=studentId, surveyId=surveyId)
        session.add(newQuestion)
        session.commit()
        session.close()

    def addAnswer(self, id, questionId, responseId, content):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        newAnswer = Answer(id=id, questionId=questionId, responseId=responseId, content=content)
        session.add(newQuestion)
        session.commit()
        session.close()

    def addSurvey(self, id, title, courseId):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        newSurvey = Survey(id=id, title=title, courseId=courseId)
        session.add(newQuestion)
        session.commit()
        session.close()

    def connectCoursetoSurvey(self, surveyId):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # connectSurvey = append surveyId to course here
        session.add(connectSurvey)
        session.commit()
        session.close()
