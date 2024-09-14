from sqlalchemy import create_engine, MetaData, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# Create the engine and base class
engine = create_engine('sqlite:///student23.db')
Base = declarative_base()

# Define the Students class
class Students(Base):
    __tablename__ = "STUDENTS"
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String(50))
    subject = Column(String(50))
    marks = Column(Integer)

# Create tables
Base.metadata.create_all(engine)

# Initialize MetaData and inspect
metadata = MetaData()
metadata.reflect(bind=engine)
inspector = inspect(engine)

# Print table details
print("Table 'STUDENTS' Details:")
columns = inspector.get_columns("STUDENTS")
for column in columns:
    print(f"Column: {column['name']} - Type: {column['type']}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add student records
students_list = [
    Students(name="a", subject="b", marks=70),
    Students(name="b", subject="c", marks=70),
    Students(name="c", subject="c", marks=70)
]

session.add_all(students_list)
session.commit()

# Query the database
all_students = session.query(Students).all()
for stu in all_students:
    print(f"{stu.id}: {stu.name} - {stu.subject} - {stu.marks}")
