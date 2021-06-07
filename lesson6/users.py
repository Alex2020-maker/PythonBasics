from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        answer = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): (el[1].strip()) if el[0] else exit(1) for el in answer}

        with open("dict_users.json", "w", encoding="utf-8") as f:
            dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
