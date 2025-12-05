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



import re

def parse_grades(grades_str):
    """Парсит строку вида 'Математика (6, 6, 8)' → ('Математика', [6,6,8])"""
    name, nums = grades_str.split("(")
    name = name.strip()
    nums = nums.replace(")", "")
    nums = [int(x) for x in nums.split(",")]
    return name, nums


def parse_line(line):
    """Парсит одну строку файла"""
    parts = line.split(",")
    
    fio = parts[0].strip()
    class_name = parts[1].strip()

    subjects_raw = ",".join(parts[2:])  # всё остальное — предметы
    subjects_raw = subjects_raw.split("),")

    subjects = {}
    for subj in subjects_raw:
        subj = subj.strip()
        if not subj.endswith(")"):
            subj += ")"
        name, nums = parse_grades(subj)
        subjects[name] = nums

    return fio, class_name, subjects


def load_students(filename):
    """Читает файл и собирает словарь по классам"""
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


def calc_total_score(student):
    """Считает сумму всех оценок ученика"""
    total = 0
    for marks in student["objects"].values():
        total += sum(marks)
    return total


def find_best_students(classes):
    """Находит лучших учеников в каждом классе"""
    best = {}

    for class_name, students in classes.items():
        max_score = max(calc_total_score(s) for s in students)
        best[class_name] = [
            s for s in students if calc_total_score(s) == max_score
        ]

    return best


def save_best(filename, best_students):
    """Записывает лучших учеников в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        for class_name, students in best_students.items():
            f.write(f"Класс {class_name}:\n")
            for s in students:
                f.write(f"  {s['fio']} — лучший ученик\n")
            f.write("\n")


# Основная программа
classes = load_students(r"C:\Users\konob\project_py\bh_homework_TK\lesson 10\students_grades.txt")
best = find_best_students(classes)
save_best("excellent_students.txt", best)

print("Готово! Лучшие ученики записаны в excellent_students.txt")


