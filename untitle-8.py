# def get_target_letter_freq(words_list, target_letter):
#     count = 0
#     for word in words_list:
#         for letter in word:
#             if letter == target_letter:
#                 count += 1

#     return count
# words = ['word', 'hello', 'world', 'well done', 'good work']
# print(get_target_letter_freq(words, 'w'))

# def get_list_of_vowel_counts(words_list):
#     result = []
#     vowels = 'AEIOUaeiou'
#     for word in words_list:
#         count = 0
#         for letter in word:
#             if letter in vowels:
#                 count += 1
#         result.append(count)

#     return result
# name_list = ["hello", "world", "morning"]
# print(get_list_of_vowel_counts(name_list))


# def print_right_angle_triangle(number_of_rows):
#     for row in range(1, number_of_rows+1):
#         for column in range(row):
#             print(column, end = "")
#         print()

# number_of_rows = 4
# print_right_angle_triangle(number_of_rows)


# def print_mirrored_right_angle_triangle(number_of_rows):
#     for row in range(1, number_of_rows+1):
#         for col in range(number_of_rows - row):
#             print(" ",end = "")
#         for col in range(row):
#             print("#",end = "")
#         print()


# number_of_rows = 4
# print_mirrored_right_angle_triangle(number_of_rows)


# def print_special_rectangle (number_of_rows, number_of_columns):
#     for row in range(1, number_of_rows+1):
#         for col in range(1,number_of_columns+1):
#             if (row+col) % 2 != 0 :
#                 print('#', end='')
#             else:
#                 print('-', end='')
#         print()
# number_of_rows = 4
# number_of_columns = 5
# print_special_rectangle(number_of_rows, number_of_columns)


# n = "-7.2"
# n = float(n)
# n = int(n)
# print(n)
# print(type(n))


import turtle
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.penup()

turtle.forward(10)
turtle.color("red")
turtle.pendown()
turtle.forward(400)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(150)
turtle.penup()

turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(220)
turtle.color("green")
turtle.pendown()
# turtle.circle(80)
for a in range(720):    
    turtle.forward(0.5)
    turtle.left(0.5)
turtle.penup()

turtle.done()


