from flask import request

def deserialize_teacher_data():
    data = request.get_json()

    name = data.get("name")
    subject = data.get("subject")
    number_of_hours = data.get("number_of_hours")

    return {
        "name": name,
        "subject": subject,
        "number_of_hours": number_of_hours
    }

def deserialize_mark_data():
    data = request.get_json()

    teacher_id = data.get("teacher_id")
    value = data.get("value")

    return {
        "teacher_id": teacher_id,
        "value": value
    }

