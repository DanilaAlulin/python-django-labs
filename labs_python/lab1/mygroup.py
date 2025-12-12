groupmates = [
    {
        "name": "Данила",
        "surname": "Алюлин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Илья", 
        "surname": "Автономов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Максим",
        "surname": "Мухачёв", 
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Виктория",
        "surname": "Молчанова",
        "exams": ["Физика", "Математика"],
        "marks": [5, 4]
    },
    {
        "name": "Евгений",
        "surname": "Камаев", 
        "exams": ["Химия", "Биология"],
        "marks": [3, 3]
    }
]


def print_students(students):
    """
    Функция для вывода списка студентов в форматированной таблице.
    """
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        exams = ', '.join(student["exams"])
        marks = ', '.join(map(str, student["marks"]))
        print(student["name"].ljust(15), student["surname"].ljust(10), str(exams).ljust(30), str(marks).ljust(20))


def calculate_average(marks):
    """
    Вспомогательная функция для расчета среднего балла.
    """
    return sum(marks) / len(marks) if marks else 0


def filter_students_by_average(students, average_mark):
    """
    Функция для фильтрации студентов по среднему баллу.
    Возвращает список студентов, у которых средний балл ВЫШЕ заданного.
    """
    filtered_students = []
    for student in students:
        student_avg = calculate_average(student["marks"])
        if student_avg > average_mark:
            filtered_students.append(student)
    return filtered_students


# Вывод полного списка студентов
print("Полный список студентов:")
print_students(groupmates)
print("\n")

# Запрос входных данных от пользователя
try:
    input_average = float(input("Введите средний балл для фильтрации: "))
except ValueError:
    print("Ошибка! Введите числовое значение.")
    exit()

# Фильтрация и вывод результата
filtered_list = filter_students_by_average(groupmates, input_average)

print(f"\nСтуденты со средним баллом выше {input_average}:")
if filtered_list:
    print_students(filtered_list)
else:
    print("Студентов с таким средним баллом не найдено.")