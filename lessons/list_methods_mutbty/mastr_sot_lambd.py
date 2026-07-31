students = [
    {'name': 'Ada', 'score': 45},
    {'name': 'Bo', 'score': 78},
    {'name': 'Chidi', 'score': 92},
]

# sorted() version — makes a new list
by_score = sorted(students, key=lambda s: s['score'], reverse=True)
print(by_score)

# .sort() version — changes students in place
students.sort(key=lambda s: s['score'], reverse=True)
print(students)

