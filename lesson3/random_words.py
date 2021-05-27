from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
listWords = []


def get_jokes(n, flag=False):

    for i in range(n):

        randomNoun = choice(nouns)
        randomAdverb = choice(adverbs)
        randomAdjective = choice(adjectives)

        listWords.append(f'{randomNoun} {randomAdverb} {randomAdjective}')

        if flag:
            nouns.remove(randomNoun)
            adverbs.remove(randomAdverb)
            adjectives.remove(randomAdjective)

    print(listWords)


num = int(input("Enter the number: "))

get_jokes(num, flag=True)
