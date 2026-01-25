students = [
    ("Arka", "Mathematics"),
    ("Martin", "Computer Science"),
    ("Sayan", "Maths"),
    ("Arka", "Biology"),
    ("Riya", "Computer Science"),
    ("Sayan", "Physics"),
    ("Ananya", "Chemistry"),
    ("Rahul", "English"),
    ("Priya", "Biology")
]

#to access all name
for tup in students:
    print(tup[0])

print("\n\n")
#to access all subjects
for tup in students:
    print(tup[1])

#to access both
for name,course in students:
    print(name," : ",course)

#adding name to set --> will be unique
students_set=set()

for tup in students:
    students_set.add(tup[0])
    #adding name

print(students_set)

#adding  to set --> will be unique
studentsCourse_set=set()

for tup in students:
    studentsCourse_set.add(tup[1])
    #adding name

print(studentsCourse_set)

#name of students study cs
for name,course in students:
    if(course=='Computer Science'):
        print(name)

