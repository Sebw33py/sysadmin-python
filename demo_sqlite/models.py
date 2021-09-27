# Can be written : from peewee import *
from peewee import (
    SqliteDatabase,
    IPField,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    CompositeKey,
    Model
)
import datetime

path_to_db = "sqlite.db"
db = SqliteDatabase(path_to_db)

class BaseModel(Model):
    class Meta:
        database = db

class Professor(BaseModel):
    first_name = CharField()
    last_name = CharField(unique=True)
    creation_date = DateTimeField(default=datetime.datetime.now)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Course(BaseModel):
    name = CharField(unique=True)
    professor = ForeignKeyField(Professor, backref="professors")
    creation_date = DateTimeField(default=datetime.datetime.now)

class Student(BaseModel):
    first_name = CharField()
    last_name = CharField(unique=True)
    creation_date = DateTimeField(default=datetime.datetime.now)

class StudentToCourse(Model):
    # Many-to-many relationship
    student = ForeignKeyField(Student)
    course = ForeignKeyField(Course)

    class Meta:
        primary_key = CompositeKey('student', 'course')