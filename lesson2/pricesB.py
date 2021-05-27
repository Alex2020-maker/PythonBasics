# Вариант B

prices = [57.4, 46.51, 97, 64.08, 54.02, 60, 44.04,
          90.03, 67.99, 55.33, 88.36, 38, 77, 66.22, 88.03, 11]

print(f"\nItWas: {id(prices)}")

prices.sort()

for i in prices:
    rub = int(i // 1)
    kop = int(f"{i % 1:.02f}"[2:])
    print(f"{rub} руб {kop:02d} коп", end=" ")

print(f"\nItBecame: {id(prices)}")

