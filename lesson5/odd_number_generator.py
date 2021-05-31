n = int(input("enter a number: "))


def odd_number(value):

    for value in range(1, value + 1, 2):
        yield value


for i in odd_number(n):
    print(i)
