# leap year checker


def is_leap(year):
    leap = False

    # Write your logic here
    leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    return leap


# year = int(input())
# print(is_leap(year))

#############################

def writeConsecutiveNumbers(n):
    final_number = ""
    number_list = list(range(1, n + 1, 1))

    for number in number_list:
        final_number += str(number)

    return final_number


#############################


def find_list(x, y, z, n):
    final_list = []

    for num_x in list(range(x + 1)):
        for num_y in list(range(y + 1)):
            for num_z in list(range(z + 1)):
                if num_x + num_y + num_z != n:
                    sub_list = [num_x, num_y, num_z]
                    final_list.append(sub_list)

    return final_list


# print(find_list(1, 1, 1, 2))
#####################################

def find_runner_up(n, arr):
    unique_list = []

    for number in sorted(arr):
        if number not in unique_list:
            unique_list.append(number)

    return unique_list.pop(len(unique_list) - 2)


# print(find_runner_up(9, [2, 3, 4, 5, 6, 7, 8, 9, 10]))

########################################

def find_second_low_students(students):
    sorted_list = sorted(students, )

    scores = []

    for student in sorted_list:
        if student[1] not in scores:
            scores.append(student[1])

    second_lowest_score = sorted(scores).pop(1)
    student_names = []

    for student in students:
        if student[1] == second_lowest_score:
            student_names.append(student[0])

    return student_names


####################################

def find_avg(students: dict, query_name: str):
    scores = students.get(query_name)

    print(format(sum(scores) / 3, '.2f'))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_marks)
    find_avg(student_marks, query_name)

##############################################