number = int(input('Enter a number up to 20: '))

if 10 < number < 20:
    print(number, "процентов")


# If the last digit is 1 (процент)
elif number % 10 == 1:
    print(number, "процент")


# If the last digit is 2, 3 or 4 (процента)
elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
    print(number, "процента")

