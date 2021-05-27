from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(value):
    answer = response.split("Valute ID=")
    for i in answer:
        if value.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


word = input("Enter currency in: ")

print(currency_rates(word))
