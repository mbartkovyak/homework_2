import requests


def test_teacher_creation():
    name = "teacher_D"
    subject = "Spanish"
    number_of_hours = 22

    request_json = {"name": name, "subject": subject, "number_of_hours": number_of_hours}

    response = requests.post(
        "http://localhost:5001/teacher",
        json=request_json
    )
    print(response.status_code)
    print(response.json())

#if __name__ == "__main__":
#    test_teacher_creation()


