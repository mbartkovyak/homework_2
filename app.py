
from flask import Flask, jsonify, request
from db import Teacher
from serializators import serialize_db_teacher
from deserializator import deserialize_teacher_data

app = Flask(__name__)

@app.route('/teacher', methods=["GET", "POST"])
def teacher_api():
    if request.method == "GET":
        teachers = Teacher.select()
        return jsonify([serialize_db_teacher(teacher) for teacher in teachers])

    elif request.method == "POST":
        data = deserialize_teacher_data()
        teacher = Teacher.create(**data)
        return jsonify(serialize_db_teacher(teacher)), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


