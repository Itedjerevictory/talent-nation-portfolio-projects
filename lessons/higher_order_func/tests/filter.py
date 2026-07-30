students = [
    {'name': 'Ada', 'score': 45},
    {'name': 'Bo', 'score': 78},
    {'name': 'Chidi', 'score': 92},
    {'name': 'Deji', 'score': 55},
]

result = list(filter(lambda item: item['score'] >= 60, students))
print(result)

