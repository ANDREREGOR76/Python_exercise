empty_dict = {}
print(type(empty_dict))
grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]
print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades
print(joel_has_grade)
kate_has_grade = "Kate" in grades
print(kate_has_grade)

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

print(joels_grade, kates_grade, no_ones_grade)