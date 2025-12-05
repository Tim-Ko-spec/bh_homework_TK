# 1.Открыть и обработать файл students_grades.txt.
# 2.Собрать все данные в словарь ниже приведенного формата.
# 3.Записать в файл "excellent_students.txt" учеников из каждого класса с наибольшим балом.
# {
#     "9A":[
#         {'fio':'fio', 
#          'objects':{
#             'mathematics':[4, 9, 7],
#             'physics':[8, 9, 8, 6],
#             ...:...
#             }
#         },
#         ...        
#     ],
#     "9Б":[
#         ...
#     ]
# }

"""Есть вероятность сбоя"""



import os
import re


def parse_subject_block(block: str):
    """
    Преобразует строку вида:
    'Математика (6, 6, 8)' → ('Математика', [6,6,8])
    """
    name, nums = block.split("(")
    name = name.strip()
    nums = nums.replace(")", "").strip()
    nums = [int(x) for x in nums.split(",")]
    return name, nums


def parse_line(line: str):
    """
    Парсит строку файла:
    'ФИО, класс, Математика(...), Русский язык(...), ...'
    """
    parts = line.split(",")

    fio = parts[0].strip()
    class_name = parts[1].strip()

    # всё, что после класса — предметы
    subjects_raw = ",".join(parts[2:])
    subject_blocks = subjects_raw.split("),")

    subjects = {}
    for block in subject_blocks:
        block = block.strip()
        if not block.endswith(")"):
            block += ")"
        name, nums = parse_subject_block(block)
        subjects[name] = nums

    return fio, class_name, subjects


def load_students(filename: str):
    classes = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            fio, class_name, subjects = parse_line(line)

            if class_name not in classes:
                classes[class_name] = []

            classes[class_name].append({
                "fio": fio,
                "objects": subjects
            })

    return classes


def total_score(student):
    """Считает сумму всех оценок ученика"""
    return sum(sum(marks) for marks in student["objects"].values())


def find_best_students(classes_dict):
    best = {}

    for class_name, students in classes_dict.items():
        max_score = max(total_score(s) for s in students)
        best[class_name] = [
            s for s in students if total_score(s) == max_score
        ]

    return best


def save_best(filename, best_students):
    with open(filename, "w", encoding="utf-8") as f:
        for class_name, students in best_students.items():
            f.write(f"Класс {class_name}:\n")
            for s in students:
                f.write(f"  {s['fio']} — лучший ученик\n")
            f.write("\n")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "students_grades.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "excellent_students.txt")

classes = load_students(INPUT_FILE)
best = find_best_students(classes)
save_best(OUTPUT_FILE, best)

print("Готово! Лучшие ученики записаны в excellent_students.txt")


