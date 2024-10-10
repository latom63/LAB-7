# Дані за зменшенням зростуу
students = {
    "Ivanov": 185,
    "Petrov": 182,
    "Sidorov": 180,
    "Kovalenko": 178,
    "Shevchenko": 175,
    "Bondarenko": 170,
    "Tkachenko": 168,
    "Lysenko": 165,
    "Pavlenko": 162,
    "Kravchenko": 160
}

# Зріст нового учня
new_student_height = 172
new_student_name = "Novachok"
# а) Прізвища і зріст всіх учнів, зріст яких менший за зріст "новенького"
smaller_students = [(name, height) for name, height in students.items() if height < new_student_height]
print("Учні, зріст яких менший за новенького:")
for name, height in smaller_students:
    print(f"{name}: {height} см")
# б) Прізвище і зріст учня, після якого слід записати "новенького"
previous_student = None
for name, height in students.items():
    if height < new_student_height:
        break
    previous_student = (name, height)
print(f"Прізвище учня, після якого слід записати новенького: {previous_student[0]}, зріст: {previous_student[1]} см")
# в) Прізвище і зріст учня, зріст якого найменше відрізняється від зросту новенького
closest_student = min(students.items(), key=lambda student: abs(student[1] - new_student_height))
print(f"Прізвище учня, зріст якого найменше відрізняється від новенького: {closest_student[0]}, зріст: {closest_student[1]} см")
print(f"Новенький учень: {new_student_name}, зріст: {new_student_height} см")
