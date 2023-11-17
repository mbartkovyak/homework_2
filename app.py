
from flask import Flask, jsonify, request
from peewee import fn

from db import Student, Teacher, Mark
from serializators import serialize_db_teacher, serialize_db_mark, serialize_db_teacher_with_marks,\
    serialize_db_mark_with_teacher, serialize_db_student_with_marks, serialize_db_student, serialize_db_mark_with_student
from deserializator import deserialize_teacher_data, deserialize_mark_data, deserialize_student_data
from validators import validate_mark_data, validate_student_data

app = Flask(__name__)

@app.route('/teachers', methods=["GET", "POST"])
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

        mark = Mark.create(**validated_data)

        return jsonify(serialize_db_mark(mark)), 201
    if request.method == "GET":
        marks = Mark.select(Mark, Teacher).join(Teacher)

        return jsonify([serialize_db_mark(mark) for mark in marks])

@app.route('/students_test', methods=["GET", "POST"])
def students_api():
    if request.method == "GET":
        # Get name from query params
        filter_name = request.args.get("name")

        students = Student.select(Student, fn.AVG(Mark.value).alias("avg_mark")).join(Mark).group_by(Student).order_by(
            fn.AVG(Mark.value).desc())

        if filter_name:
            students = students.where(Student.name.contains(filter_name))

        return jsonify([serialize_db_student(student) for student in students])


    elif request.method == "POST":
        data = deserialize_student_data()

        student = Student.create(**data)

        return jsonify(serialize_db_student(student)), 201


@app.route('/teacher_id/<int:teacher_id>', methods=["GET","PATCH","DELETE"])
def teacher_id_api(teacher_id):

    if request.method == "GET":

        teacher = Teacher.get_or_none(id=teacher_id)

        return jsonify(serialize_db_teacher(teacher))

    if request.method == "PATCH":

        data = request.get_json()

        id = data.get("id")
        name = data.get("name")
        subject = data.get("subject")
        number_of_hours = data.get("number_of_hours")

       # validated_data = validate_teacher_data(data)

        teacher = Teacher.get_or_none(id=teacher_id)

        if name:
            teacher.name = name

        teacher.save()
        if subject:
            teacher.subject = subject

        teacher.save()
        if number_of_hours:
            teacher.number_of_hours = number_of_hours

        teacher.save()

        return jsonify({"id": id, "name": name, "subject": subject, "number_of_hours": number_of_hours}), 201

    elif request.method == "DELETE":

        teacher = Teacher.delete().where(Teacher.id==teacher_id).execute()

        return "",204


@app.route('/mark_student_id_api/<int:student_id>', methods=["GET","PATCH","DELETE"])
def mark_student_id_api(student_id):

    if request.method == "DELETE":

        mark = Mark.delete().where(Mark.student_id==student_id).execute()

        return "",204


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


