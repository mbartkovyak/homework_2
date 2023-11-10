from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('sqlite3.db')

class BaseModel(Model):
    class Meta:
        database = db


class Teacher(BaseModel):
    name = CharField()
    subject = CharField()
    number_of_hours = IntegerField()

if __name__ == "__main__":
    db.connect()
    db.create_tables([Teacher])
    db.close()