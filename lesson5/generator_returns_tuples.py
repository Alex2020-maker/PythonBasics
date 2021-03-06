from itertools import zip_longest, islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

answer = (i for i in zip_longest(tutors, klasses))

print(type(answer))
print(*islice(answer, 7), sep="\n")
