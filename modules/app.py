import modules.utils  # tüm module ü import etmek istersek
from modules.utils import find_max  # spesifik bir method import etmek istersek

numbers = [3, 2, 5, 7, 12, 88, 1, 10]

max_number = find_max(numbers)
print(max_number)
print(modules.utils.find_max(numbers))