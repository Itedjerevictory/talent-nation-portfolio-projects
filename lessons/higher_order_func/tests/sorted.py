students = [
    {'name': 'Ada', 'score': 45},
    {'name': 'Bo', 'score': 78},
    {'name': 'Chidi', 'score': 92},
    {'name': 'Deji', 'score': 55},
]

result = sorted(students, key=lambda item: item['score'], reverse=True)
print(result)



# Use sorted() with key= to arrange the students from highest score to lowest.
