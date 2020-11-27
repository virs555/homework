school =[
    {'school_class': '4a', 'scores': [4,5,5,3,4]}, 
    {'school_class': '4b', 'scores': [3,2,4,5,3]}, 
    {'school_class': '4e', 'scores': [3,2,4,3,4]}
]

avg_school_score = 0
scores_counter = 0
summ = 0

for score in school:
    for i in score['scores']:
        avg_school_score += i
        scores_counter += 1
    summ += avg_school_score
    print(f"Средняя оценка в {score['school_class']}: {avg_school_score / len(score['scores'])}")
    avg_school_score = 0

print(f'Средняя оценка по школе: {summ / scores_counter}')

