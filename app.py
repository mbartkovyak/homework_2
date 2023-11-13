
from flask import Flask, jsonify, request
from db import Teacher, Mark
from serializators import serialize_db_teacher, serialize_db_mark, serialize_db_teacher_with_marks, serialize_db_mark_with_teacher
from deserializator import deserialize_teacher_data, deserialize_mark_data
from Validators import validate_mark_data

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

@app.route('/marks', methods=["GET", "POST"])
def marks_api():
    if request.method == "POST":
        data = deserialize_mark_data()

        validated_data = validate_mark_data(data)
        # validated_data["teacher"] = teacher

        mark = Mark.create(**validated_data)
        # mark.teacher = teacher

        return jsonify(serialize_db_mark(mark)), 201
    if request.method == "GET":
        marks = Mark.select(Mark, Teacher).join(Teacher)

        return jsonify([serialize_db_mark(mark) for mark in marks])




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


