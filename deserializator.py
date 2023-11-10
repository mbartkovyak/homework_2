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

