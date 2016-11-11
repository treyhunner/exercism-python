from collections import defaultdict
from itertools import chain


STUDENTS = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry',
]


PLANTS = {'R': 'Radishes', 'C': 'Clover', 'G': 'Grass', 'V': 'Violets'}


def get_student_plants(diagram, students):
    row1, row2 = [
        [PLANTS[p] for p in row]
        for row in diagram.splitlines()
    ]
    plant_lists = row1[::2], row1[1::2], row2[::2], row2[1::2]
    return {
        student: plants
        for student, *plants in zip(sorted(students), *plant_lists)
    }


class Garden:

    def __init__(self, diagram, *, students=STUDENTS):
        self.student_plants = get_student_plants(diagram, sorted(students))

    def plants(self, name):
        return self.student_plants[name]
