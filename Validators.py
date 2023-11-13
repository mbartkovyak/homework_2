from db import Teacher


class ValidationError(Exception):
    pass


def validate_teacher_data(data):
    name = data.get("name")
    number_of_hours = data.get("number_of_hours")

    if not (name and number_of_hours):
        raise ValidationError("name and number_of_hours are required")

    if not isinstance(number_of_hours, int):
        raise ValidationError("number_of_hours must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")

    if number_of_hours < 0:
        raise ValidationError("number_of_hours must be positive")
    if name == "":
        raise ValidationError("name must not be empty")


def validate_mark_data(data):
    teacher_id = data.get("teacher_id")
    value = data.get("value")

    teacher = Teacher.get_or_none(id=teacher_id)

    if not teacher:
        raise ValidationError("teacher with such id does not exist")

    if not (teacher_id and value):
        raise ValidationError("teacher_id and value are required")

    if not isinstance(teacher_id, int):
        raise ValidationError("teacher_id must be integer")
    if not isinstance(value, int):
        raise ValidationError("value must be integer")

    if value < 0:
        raise ValidationError("value must be positive")

    data["teacher"] = teacher
    return data
