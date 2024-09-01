# 10.1
# from pathlib import Path
# path = Path('learning_python.txt')
# contents = path.read_text()
# contents1 = contents.splitlines()
# for a in contents1:
#     print(a)

# 10.2
# from pathlib import Path
# path = Path('learning_python.txt')
# contents = path.read_text()
# contents1 = contents.splitlines()
# print(contents1)
# a=contents.replace('Python','C++')
# print(a)

# 10.4
# from pathlib import Path

# path = Path("guest.txt")
# A = 0
# x = ""
# while A != 3:
#     x += input("please input your name: ")
#     x += "\n"
#     A += 1
# contents = path.write_text(x)

# 10.6
# number = input("please input a number: ")
# number1 = input("please input a number: ")
# try:
#     number = int(number)
#     number1 = int(number1)
#     print(number + number1)

# except ValueError:
#     print("please input number not letters")


# 10.7
# number = input("please input a number: ")
# number1 = input("please input a number: ")
# x = 0
# try:
#     while x !=3:
#         number = int(number)
#         number1 = int(number1)
#         xxa = number + number1
#         x+=1

#     print(xxa)

# except ValueError:
#     print("please input number not letters")


# 10.8
# from pathlib import Path

# try:
#     path = Path("dog.txt")
#     contents = path.read_text()
#     contents1 = contents.splitlines()
#     print(contents1)

#     path1 = Path("cat.txt")
#     contents2 = path1.read_text()
#     contents3 = contents2.splitlines()
#     print(contents3)

# except FileNotFoundError:
#     print("please put the file on the right place.")


# 10.9
# from pathlib import Path

# try:
#     path = Path("dog.txt")
#     contents = path.read_text()
#     contents1 = contents.splitlines()
#     print(contents1)

#     path1 = Path("cat.txt")
#     contents2 = path1.read_text()
#     contents3 = contents2.splitlines()
#     print(contents3)

# except FileNotFoundError:
#     pass


# # 10.10
# from pathlib import Path
# path = Path("dog.txt")
# ??????


# 10.11
# from pathlib import Path
# import json

# path = Path("new.txt")
# number = input("please input a number wich you like: ")
# contents = json.dumps(number)
# path.write_text(contents)

# contents1 = contents.splitlines()
# print(f"I know your favorite number! It's{contents1}")

# 10.12
# from pathlib import Path
# import json

# path = Path("new.txt")
# if path.exists:
#     contents = path.read_text()
#     number = json.loads(contents)
#     print(f"I know your favorite number! It's{contents}")

# else:
#     number = input("please input a number wich you like: ")
#     contents = json.dumps(number)
#     path.write_text(contents)

# 10.13
# from pathlib import Path
# import json


# def greetuser():
#     """问候用户，并指出其名字"""
#     path = Path("username.json")
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back,{username}!")
#     else:
#         username = input("What is your name?")
#         Gender = input("what is your gender?")
#         age = input("how old are you?")
#         contents = json.dumps(username)
#         contents1 = json.dumps(Gender)
#         contents2 = json.dumps(age)
#         contents = contents, contents1, contents2
#         path.write_text(contents)
#         print(f"We'll remember you when you come back,{username}!")


# greetuser()

# # 10.14
# from pathlib import Path
# import json


# def greet_user():
#     """问候用户，并指出其名字"""
#     path = Path("username.json")
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back,{username}!")
#     else:
#         username = input("What is your name?")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back,{username}!")

# greet_user()


# def get_formatted_name(frist, last):
#     """生成格式规范的姓名"""
#     full_name = f"{frist} {last}"
#     return full_name.title()



class Employee:
    def __init__(self,first_name,last_name,annual_salary,add = 500):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.add = add
    
    def give_raise(self):
        self.annual_salary += self.add
        return self.annual_salary
