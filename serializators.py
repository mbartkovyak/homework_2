from db import Teacher


def serialize_db_teacher(teacher: Teacher):
    return {
        "id": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject,
        "number_of_hours": teacher.number_of_hours
    }