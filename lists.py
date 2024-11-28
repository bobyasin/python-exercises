mylist = ["apple", "banana", "cherry", 2, True]

print(mylist)

my_list = [1, 2, 3, 4, 5, 6, 9, 7, 12, 102, 551, 98, 2, 2, 1, 12, 102]
sorted_list = my_list.sort(reverse=True)

print(my_list[0])

# 2D list

my_2d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in my_2d_list:
    for item in row:
        print(item)

my_list.append(20)
print(my_list)

# my_list.clear()
# print(my_list)

print(5 in my_list)
print(my_list.count(2))
copy_of_my_list = my_list.copy()

# case : remove dublicates in a list

unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print(unique_list)