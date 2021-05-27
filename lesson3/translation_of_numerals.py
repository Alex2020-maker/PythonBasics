n = str(input("Enter the numeral: "))


def num_translate(num):

    listNum = {"zero": "ноль", "one": "один", "two": "два",
               "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь",
               "nine": "девять", "ten": "десять"}

    print(listNum.get(num))
    return


num_translate(n)
