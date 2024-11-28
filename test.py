# String

message = '''
This is a 
multiline message!
!
'''
# print(message)

single_line_message = 'Python Learning'
print(single_line_message[:])  # prints start index (default 0) to end index (len of string)

copy_string = single_line_message[:]  # makes a copy of string
print(copy_string)

# formatted strings
first_name = 'Yasin'
last_name = 'babaoğlu'
full_name = f'{first_name} {last_name}'
print(full_name)

# String methods
tutorial = 'learning python'
print(len(tutorial))
print(tutorial.capitalize())
print(full_name.upper())
print('py' in tutorial)
print(tutorial.title())
print('...' in tutorial)

# Operators

print(10 / 3)  # float
print(10 // 3)  # integer
print(10 ** 3)  # power
print(10 % 3)  # mod

x = 10
print(x)
x += 3
print(x)