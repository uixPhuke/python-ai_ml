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


dist={}
print(dist)
for name,course in students:
    if(dist.get(name)==None):
        dist.update({name: set()})
        dist[name].add(course)
    else:
        dist[name].add(course)
    

print(dist)