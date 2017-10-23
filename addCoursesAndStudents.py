from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Course, Student

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

# Insert Courses in course tables
newCourse = Course(title="", semester="")
session.add(newCourse)
session.commit()

# Insert Student in student tables
newStudent = Student(id="")
session.add(newStudent)
session.commit()
