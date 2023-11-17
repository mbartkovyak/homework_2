from datetime import datetime

from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField

db = SqliteDatabase('sqlite3.db')


class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    name = CharField()
    age = IntegerField()


class Teacher(BaseModel):
    name = CharField()
    subject = CharField()
    number_of_hours = IntegerField()

class Mark(BaseModel):
    teacher = ForeignKeyField(Teacher, backref='marks')
    student = ForeignKeyField(Student, backref='marks')
    value = IntegerField()
    timestamp = DateTimeField(default=datetime.now)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Teacher, Mark, Student])
    db.close()