def AmountOfCubes(num):

    result = 0

    while num != 0:
        result += num % 10
        num //= 10

    return result


listNum = [i ** 3 for i in range(1, 1001, 2)]

result_one = sum(filter(lambda num: AmountOfCubes(num) % 7 == 0, listNum))
result_two = sum(filter(lambda num: AmountOfCubes(num + 17) % 7 == 0, listNum))

print(result_one)
print(result_two)
