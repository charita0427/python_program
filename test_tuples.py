grades = {"Alice": 88, "Bob": 73, "Dan": 95, "Cherry": 61, "Claire": 83}

total = 0
for name in grades:
    total = total + grades[name]
average = total / len(grades)
print("Class average:", average)

top_name = ""
top_score = 0
for name in grades:
    if grades[name] > top_score:
        top_name = name
        top_score = grades[name]
print("Highest score:", top_name, top_score)

lookup = input("Look up a student: ")
print("Score:", grades.get(lookup, "Not found"))


