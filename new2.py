import random
import math
# class integer:
#     def __init__(self, number):
#         self.number = number
#         self.mynature = []
#         self.myprime = []
#         self.twin_prime1 = []
#         self.random0 = list(random.randint(1,50) for num in range(20))
#         self.integer = list(range(-number, number+1))

#     def nature(self):
#         for entry in self.integer:
#             if entry > 0:
#                 self.mynature.append(entry)

#     def prime(self):
#         for a in self.mynature:
#             c = 0
#             if a == 1:
#                 continue
#             else:
#                 for i in range(2, round(math.sqrt(a))+1):

#                     if a % i == 0:
#                         c = 1
#                         break
#                 if c == 0:
#                     self.myprime.append(a)
#         print(self.myprime)

#     def twin_prime(self):
#         for idx in range(0,len(self.myprime)-1):
#             if self.myprime[idx]+2 == self.myprime[idx+1]:
#                 self.twin_prime1.append([self.myprime[idx],self.myprime[idx + 1]])
#         print(self.twin_prime1)
#         print(f"{self.number}以内孪生质数有",len(self.twin_prime1),"对")

# number = 100
# num = integer(number)
# num.nature()
# num.prime()
# num.twin_prime()


# def buble():
#     csa = [random.randint(1,50)for a in range(10)]
#     print(csa)
#     for a in range(len(csa)):
#         for index in range(len(csa)-1):
#             if csa[index] >=csa[index+1]:
#                 csa[index], csa[index + 1] = csa[index + 1], csa[index]

#     print(csa)

# buble()

def select_sort():
    csa = [random.randint(1, 50) for a in range(10)]
    print(csa)
    for index in range(len(csa)-1):
        value = csa[index]
        position = index
        for a in range(index+1,len(csa)):
            if value > csa[a]:
                value,position = csa[a],a

        csa[index], csa[position] = csa[position] , csa[index]
    print(csa)

select_sort()