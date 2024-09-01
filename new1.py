import random
class integer:
    def __init__(self, number):
        self.mynature = []
        self.myodd = []
        self.myeven = []
        self.myprime = []
        self.sortlist = []
        self.random3 = []
        self.random0 = list(random.randint(1,50) for num in range(20))
        self.integer = list(range(-number, number+1))

    def random1(self):
        print(self.random0)
        self.sortlist = sorted(self.random0)
        print(self.sortlist)

    def random2(self):
        print(self.random0)
        self.nature()
        for a in self.random0:
            if a in self.mynature:
                continue
            else:
                if a not in self.random3:
                    self.random3.append(a)
        self.random3 += self.mynature
        self.random3 = set(self.random3)
        self.random3 = list(self.random3)
        # for a in self.mynature:
        #     if a not in self.random3:
        #         self.random3.append(a)
        self.random3.sort()
        print(self.random3)

    def nature(self):
        for entry in self.integer:
            if entry > 0:
                self.mynature.append(entry)

    def odd_even(self):
        for a in self.integer:
            if a % 2 == 0:
                self.myeven.append(a)

            else:
                self.myodd.append(a)

    def prime(self):
        for a in self.mynature:
            c = 0
            if a == 1:
                continue
            else:
                for i in range(2, a):

                    if a % i == 0:
                        c = 1
                        break
                if c == 0:
                    self.myprime.append(a)

    def print_number(self):
        while True:
            type = input("what answer you want: ")
            if type == "integer":
                print(self.integer)
            elif type == "nature":
                print(self.mynature)
            elif type == "random":
                print(self.random0)
            elif type == "random1":
                self.random1()
            elif type == "random2":
                self.random2()
            elif type == "odd":
                print(self.myodd)
            elif type == "even":
                print(self.myeven)
            elif type == "prime":
                print(self.myprime)
            elif type == "stop":
                break

number = 11
num = integer(number)
num.nature()
num.odd_even()
num.prime()
num.print_number()


# def modular():
#     num = int(input("input a number: "))
#     num1 = int(input("input a devide number: "))
#     while True:
#         if num1<=0:
#             num1 = int(input("input again: "))
#         else:
#             break
#     num2 = num % num1
#     if num<0:
#         while True:
#             if num<0:
#                 num+=num1
#             elif 0<= num < num1:
#                 break
#         print(num)

#     elif 0<=num<num1:
#         print(num)
    
#     else:
#         while True:
#             if num >= num1:
#                 num = num-num1
#             elif 0<= num < num1:
#                 break
#         print(num)
    
#     if num2 == num:
#         print("same")
#     else:
#         print("not same")
# modular()
