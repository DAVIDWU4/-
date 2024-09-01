# def recurrence(n):

#     if n == 1:
#         a0 = 1
#         return a0
#     else:
#         an = 3*recurrence(n-1)-1
#         return an

# print(recurrence(100))

# def test1(n):
#     if n == 1:
#         an = 0
#     elif n==2:
#         an = 1
#     else:
#         an = test1(n-1)+test1(n-2)
#     return an
# print(test1(1))
# print(test1(2))
# print(test1(3))
# print(test1(100))

# def test2(n):
#     if n==1:
#         an = 0
#     else:
#         an = 3*test2(n-1)-1
#     return an
# print(test2(100))

# def test3(n):
#     if n==1:
#         an = 0
#     elif n==2:
#         an = 1
#     else:
#         an = 2*test3(n-1)-test3(n-2)
#     return an
# print(test3(1))
# print(test3(2))
# print(test3(3))
# print(test3(4))
# print(test3(100))

# def test4(n):
#     if n==1:
#         an = 1
#     else:
#         an = n*test4(n-1)
#     return an
# print(test4(1))
# print(test4(2))
# print(test4(3))
# print(test4(4))
# print(test4(100))


# list1 = [1,5,7,9]
# x = 3
# if x in list1:
#     print("yes")
# else:
#     print("no")


# class car(object):
#     def __init__(self, length = 100, color = "red"):
#         self.length = length
#         self.color = color
#         print("1")
#     def type_car(self, price):
#         print(self.length,self.color,price)

# aodi = car(100,"green")
# aodi.type_car(100)

class integer:
    def __init__(self,number):
        self.mynature = []
        self.myodd = []
        self.myeven = []
        self.myprime = {}
        self.number = set(range(-number,number))

    def nature(self):
        print(self.number)
        for entry in self.number:
            if entry >=0:
                self.mynature.append(entry)

    def odd_even(self):
        for a in self.number:
            if a % 2 == 0:
                self.myeven.append(a)

            else:
                self.myodd.append(a)

    def prime(self):
        for a in self.mynature:
            print(self.mynature)
            c = 0
            for i in (2,a):
                if a % i == 0:
                    c = 1
                    break
            if c == 0:
                print(f"{a} is prime")

    def print_number(self):
        print(self.mynature)
        print(self.myodd)
        print(self.myeven)
number = 4
num = integer(number)
num.mynature()
# num.odd_even()
num.prime()
# num.print_number()
