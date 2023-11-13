from db import Teacher, Mark


def serialize_db_teacher(teacher: Teacher):
    return {
        "id": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject,
        "number_of_hours": teacher.number_of_hours
    }



def serialize_db_mark(mark: Mark):
    return {
        "id": mark.id,
        "value": mark.value,
        "timestamp": mark.timestamp,
    }


def serialize_db_teacher_with_marks(teacher: Teacher):
    return {
        **serialize_db_teacher(teacher),
        "marks": [serialize_db_mark(mark) for mark in teacher.marks]
    }


def serialize_db_mark_with_teacher(mark: Mark):
    return {
        **serialize_db_mark(mark),
        "teacher": serialize_db_teacher(mark.teacher)
    }
