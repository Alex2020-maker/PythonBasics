number = str(input("Enter the numeral: "))


def num_translate_adv(myKey):

    dictNum = {"zero": "ноль", "one": "один", "two": "два",
               "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь",
               "nine": "девять", "ten": "десять"}

    if number.istitle():
        value = number.lower()
        print(dictNum.get(myKey).title())
    else:
        print(dictNum.get(myKey))


num_translate_adv(number)
