# Can be written : from peewee import *
from peewee import (
    SqliteDatabase,
    IPField,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    CompositeKey,
    SmallIntegerField,
    Model
)
import datetime

path_to_db = "sqlite.db"
db = SqliteDatabase(path_to_db)

class BaseModel(Model):
    class Meta:
        database = db

class Professor(BaseModel):
    id = SmallIntegerField(unique=True, primary_key=True)
    first_name = CharField()
    # It is a test script, do not make it unique
    # last_name = CharField(unique=True)
    last_name = CharField()
    creation_date = DateTimeField(default=datetime.datetime.now)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Course(BaseModel):
    id = SmallIntegerField(unique=True, primary_key=True)
    # It is a test script, do not make it unique
    # name = CharField(unique=True)
    name = CharField()
    professor = ForeignKeyField(Professor, backref="professors")
    creation_date = DateTimeField(default=datetime.datetime.now)

class Student(BaseModel):
    id = SmallIntegerField(unique=True, primary_key=True)
    first_name = CharField()
    # It is a test script, do not make it unique
    # last_name = CharField(unique=True)
    last_name = CharField()
    creation_date = DateTimeField(default=datetime.datetime.now)