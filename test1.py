# import math
# area = float(input("Enter an area of a circle: "))
# radius =math.sqrt(area/math.pi)
# print(f"The radius is {round(radius, 1)}")


# def divide_numbers(a, b):
#     try:
#         result = a / b
#         print(f"The result is: {result}")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed!")
#     except TypeError:
#         print("Error: Inputs must be numbers!")
#     except Exception as e:
#         print(f"Unknown error: {e}")
#     finally:
#         print("Operation completed.")

# divide_numbers(10, 2)
# divide_numbers(10, 0)
# divide_numbers(10, "a")

# def divide(numerator, denominator):
#     if (type(denominator) is not int and type(denominator) is not float or type(numerator) is not int and type(numerator) is not float):
#         print('Error: one or more operands' + ' is not a number')
#     elif denominator == 0:
#         print('Error: cannot divide by zero')
#     else:
#         return numerator / denominator

# print(divide(5, 'hello'))

# my_list = [1, 2, 3]

# try:
#     index = int(input("Enter an index: "))
#     print(my_list[index])
# except IndexError:
#     print("Error: Index is out of range. Enter a valid index between 0 and",len(my_list) - 1,)
# except ValueError:
#     print("Error: Invalid input. Please enter a numeric index.")


# my_list = [1, 2, 3]

# while True:
#     try:
#         index = int(input('Enter an index: '))
#         print(my_list[index])
#         break
#     except IndexError:
#         print("Error: Index is out of range. Enter a valid index between 0 and",len(my_list) - 1,)
#     except ValueError:
#         print("Error: Invalid input. Please enter a numeric index.")

# my_dict = {"test1": 1, "test2": 2}

# key = input("Enter a key: ")
# print(my_dict[key])


# my_dict = {"test1": 1, "test2": 2}

# try:
#     key = input("Enter a key: ")
#     print(my_dict[key])
# except KeyError:
#     print("Invalid Key! Please enter a valid key ('test1' or 'test2').")

# 5.1 A 5.2 A


# def get_position(data, index):
#     temp = data[index]
#     sorted_list = sorted(data)
#     position = sorted_list.index(temp)
#     return position

# a_list1 = [10, 14, 29, 12, 56]
# print(get_position(a_list1, 3))

# a_list2 = [3, 15, 25, 37, 18]
# print(get_position(a_list2, 4))
