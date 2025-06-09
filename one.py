import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT
               )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instructor TEXT
               )
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY (student_id) REFERENCES students(id),
               FOREIGN KEY (course_id) REFERENCES courses(course_id),
               PRIMARY KEY (student_id, course_id)
               )
               

               ''')

while True:
    print("1.Додати студента")
    print("2.Додати курс")
    print("3.Показати студентів")
    print("4.Показати курси")
    print("5. Зареєструвати на курс")
    print("6. Показати студентів на курсі")
    print("7. Вийти")
    choice = input("Оберіть від 1-7")

    if choice =="1":
        name = input("Введіть імя")
        age = int(input("Введіть вік"))
        major = input("введіть спец. студента")
        cursor.execute("INSERT INTO students (name,age,major) VALUES (?,?,?)",(name,age,major))
        conn.commit()