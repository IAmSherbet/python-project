from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base();

class Question(Base):
    _tablename_ = 'question'
    # Here we define the columns for the question table
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    surveyId = Column(Integer, ForeignKey('survey.id'))

class Response(Base):
    _tablename_ = 'response'
    id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('student.id'))
    surveyId = Column(Integer, ForeignKey('survey.id'))

class Answer(Base):
    _tablename_ = 'answer'
    id = Column(Integer, primary_key=True)
    questionId = Column(Integer, ForeignKey('question.id'))
    responseId = Column(Integer, ForeignKey('response.id'))
    content = Column(String, nullable=False)

class Student(Base):
    _tablename_ = 'student'
    id = Column(Integer, primary_key=True)

class Course(Base):
    _tablename_ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    semester = Column(String(250), nullable=False)
    surveyId = Column(Integer, ForeignKey('survey.id'))

class Survey(Base):
    _tablename_ = 'survey'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    courseId = Column(Integer, ForeignKey('course.id'))

try:
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///database.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

except:
    print("Survey already there.")
