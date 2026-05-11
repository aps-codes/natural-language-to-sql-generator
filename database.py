import sqlite3

# connect database
connection = sqlite3.connect("school.db")

# cursor create
cursor = connection.cursor()

# create students table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENTS(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    class INTEGER,
    roll_no INTEGER,
    gender TEXT,
    maths_marks INTEGER,
    science_marks INTEGER,
    english_marks INTEGER,
    percentage REAL,
    attendance INTEGER,
    result TEXT
)
"""

cursor.execute(table_info)

# delete old data
cursor.execute("DELETE FROM STUDENTS")

# reset auto increment id
cursor.execute("DELETE FROM sqlite_sequence WHERE name='STUDENTS'")

# student data
students_data = [

    ("Aarav Sharma", 9, 1, "Male", 95, 91, 89, 91.67, 96, "Pass"),
    ("Priya Singh", 9, 2, "Female", 88, 85, 90, 87.67, 92, "Pass"),
    ("Rohan Verma", 9, 3, "Male", 45, 52, 48, 48.33, 70, "Pass"),
    ("Sneha Yadav", 9, 4, "Female", 76, 80, 79, 78.33, 88, "Pass"),
    ("Vivek Patel", 9, 5, "Male", 29, 40, 35, 34.67, 60, "Fail"),
    ("Aditi Chauhan", 9, 6, "Female", 67, 70, 72, 69.67, 80, "Pass"),
    ("Mohit Saini", 9, 7, "Male", 38, 42, 35, 38.33, 64, "Fail"),
    ("Kiran Yadav", 9, 8, "Female", 82, 79, 85, 82.00, 90, "Pass"),
    ("Harsh Gupta", 9, 9, "Male", 91, 89, 94, 91.33, 95, "Pass"),
    ("Tanvi Mishra", 9, 10, "Female", 58, 62, 60, 60.00, 76, "Pass"),
    ("Aryan Singh", 9, 11, "Male", 47, 50, 45, 47.33, 68, "Pass"),
    ("Pallavi Jain", 9, 12, "Female", 99, 97, 98, 98.00, 99, "Pass"),
    ("Nitin Kumar", 9, 13, "Male", 30, 28, 35, 31.00, 58, "Fail"),
    ("Riya Sharma", 9, 14, "Female", 73, 75, 78, 75.33, 84, "Pass"),
    ("Dev Malhotra", 9, 15, "Male", 65, 69, 71, 68.33, 81, "Pass"),


    ("Aditya Raj", 10, 1, "Male", 92, 90, 94, 92.00, 95, "Pass"),
    ("Muskan Gupta", 10, 2, "Female", 85, 88, 91, 88.00, 90, "Pass"),
    ("Rahul Kumar", 10, 3, "Male", 33, 37, 30, 33.33, 65, "Fail"),
    ("Kajal Mishra", 10, 4, "Female", 71, 75, 70, 72.00, 84, "Pass"),
    ("Ankit Pal", 10, 5, "Male", 56, 60, 58, 58.00, 77, "Pass"),
    ("Sakshi Verma", 10, 6, "Female", 79, 81, 84, 81.33, 87, "Pass"),
    ("Aman Yadav", 10, 7, "Male", 28, 35, 32, 31.67, 59, "Fail"),
    ("Khushi Patel", 10, 8, "Female", 94, 96, 93, 94.33, 97, "Pass"),
    ("Rajat Singh", 10, 9, "Male", 61, 63, 65, 63.00, 79, "Pass"),
    ("Meena Sharma", 10, 10, "Female", 74, 77, 79, 76.67, 86, "Pass"),
    ("Sourabh Kumar", 10, 11, "Male", 48, 50, 46, 48.00, 71, "Pass"),
    ("Anjali Gupta", 10, 12, "Female", 89, 92, 90, 90.33, 93, "Pass"),
    ("Rohit Pal", 10, 13, "Male", 33, 30, 29, 30.67, 60, "Fail"),
    ("Payal Mishra", 10, 14, "Female", 85, 87, 88, 86.67, 91, "Pass"),
    ("Lakshya Jain", 10, 15, "Male", 69, 72, 70, 70.33, 82, "Pass"),

    ("Neha Sharma", 11, 1, "Female", 97, 95, 96, 96.00, 98, "Pass"),
    ("Arjun Singh", 11, 2, "Male", 68, 72, 70, 70.00, 82, "Pass"),
    ("Pooja Verma", 11, 3, "Female", 41, 39, 44, 41.33, 69, "Pass"),
    ("Ritesh Yadav", 11, 4, "Male", 25, 31, 28, 28.00, 55, "Fail"),
    ("Simran Kaur", 11, 5, "Female", 81, 84, 79, 81.33, 89, "Pass"),
    ("Shivani Rai", 11, 6, "Female", 87, 90, 89, 88.67, 92, "Pass"),
    ("Manish Kumar", 11, 7, "Male", 36, 38, 34, 36.00, 63, "Fail"),
    ("Ruchi Singh", 11, 8, "Female", 92, 94, 91, 92.33, 96, "Pass"),
    ("Aakash Verma", 11, 9, "Male", 66, 68, 64, 66.00, 78, "Pass"),
    ("Komal Patel", 11, 10, "Female", 72, 75, 77, 74.67, 85, "Pass"),
    ("Yuvraj Sharma", 11, 11, "Male", 55, 58, 54, 55.67, 74, "Pass"),
    ("Tanya Gupta", 11, 12, "Female", 98, 97, 99, 98.00, 99, "Pass"),
    ("Dheeraj Pal", 11, 13, "Male", 29, 31, 27, 29.00, 57, "Fail"),
    ("Mansi Yadav", 11, 14, "Female", 81, 83, 85, 83.00, 88, "Pass"),
    ("Kabir Thakur", 11, 15, "Male", 63, 67, 65, 65.00, 80, "Pass"),

    ("Karan Patel", 12, 1, "Male", 90, 93, 91, 91.33, 94, "Pass"),
    ("Ishita Gupta", 12, 2, "Female", 86, 88, 90, 88.00, 91, "Pass"),
    ("Deepak Kumar", 12, 3, "Male", 52, 55, 50, 52.33, 73, "Pass"),
    ("Nisha Yadav", 12, 4, "Female", 34, 36, 32, 34.00, 66, "Fail"),
    ("Yash Thakur", 12, 5, "Male", 74, 78, 80, 77.33, 85, "Pass"),
    ("Sanya Kapoor", 12, 6, "Female", 91, 94, 92, 92.33, 95, "Pass"),
    ("Vikas Sharma", 12, 7, "Male", 42, 39, 41, 40.67, 67, "Pass"),
    ("Nandini Singh", 12, 8, "Female", 96, 98, 97, 97.00, 99, "Pass"),
    ("Rohit Verma", 12, 9, "Male", 57, 60, 59, 58.67, 76, "Pass"),
    ("Priti Yadav", 12, 10, "Female", 77, 80, 82, 79.67, 87, "Pass"),
    ("Abhishek Raj", 12, 11, "Male", 31, 33, 29, 31.00, 61, "Fail"),
    ("Diya Malhotra", 12, 12, "Female", 88, 90, 91, 89.67, 93, "Pass"),
    ("Kunal Gupta", 12, 13, "Male", 70, 73, 75, 72.67, 84, "Pass"),
    ("Suhani Jain", 12, 14, "Female", 84, 86, 88, 86.00, 90, "Pass"),
    ("Varun Patel", 12, 15, "Male", 49, 52, 50, 50.33, 72, "Pass")
]

# insert query
insert_query = """
INSERT INTO STUDENTS(
    student_name,
    class,
    roll_no,
    gender,
    maths_marks,
    science_marks,
    english_marks,
    percentage,
    attendance,
    result
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# insert all data
cursor.executemany(insert_query, students_data)

# save changes
connection.commit()

print("Student data inserted successfully")

# class 10 failed students
data = cursor.execute(
    "SELECT * FROM STUDENTS WHERE class = 10 AND result = 'Fail'"
)

print("\nClass 10 Failed Students\n")

for row in data:
    print(row)

# failed students
fail_students = cursor.execute(
    "SELECT * FROM STUDENTS WHERE result = 'Fail'"
)

print("\nFailed Students\n")

for row in fail_students:
    print(row)

# top 5 students
top_students = cursor.execute(
    "SELECT * FROM STUDENTS ORDER BY percentage DESC LIMIT 5"
)

print("\nTop 5 Students\n")

for row in top_students:
    print(row)

# low attendance students
low_attendance = cursor.execute(
    "SELECT * FROM STUDENTS WHERE attendance < 70"
)

print("\nLow Attendance Students\n")

for row in low_attendance:
    print(row)
