my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(my_list)):

    temporary_list = my_list[i].split(" ")
    hm_indexes = len(temporary_list) - 1
    temporary_name = temporary_list[hm_indexes]
    name = temporary_name.lower().title()

    print(f"Привет, {name}!")
