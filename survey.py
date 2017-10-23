from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Question(Base):
    _tablename_ = 'QUESTION'
    questionId = Column(Integer, primary_key=True)
    title = Column(String)


class Survey(object):
    def create_table(self):
        engine = create_engine('sqlite:///surveys.db')
        Base.metadata.create_all(engine)

    def insert_question(self, id, question):
        engine = create_engine('sqlite:///surveys.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        newQuestion = Question(id=id, question=question)
        session.add(newQuestion)
        session.commit()
        session.close()


survey = Survey()
try:
    survey.create_table()
except:
    print("Survey already there.")

#Insert records into the table
#survey.insert_question('003','What is your name?')

#Search the tables in the database
#library.search_quesiton('Agile Design')
