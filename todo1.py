# list2 = list(range(1,8))
# # list1 = ["f","sda4,","g"]
# # tuple1 = (1,6,23,3,4)
# tuple2 = tuple((1,6,23,3,4))
# # set1 = {"sadad","fdasf","hjlkk"}
# set2 = set(("sadad","fdasf","hjlkk"))
# # dict1 = {"fadsdf":"1","ewr":"7","adfd":00}
# dict2 = dict(fadsdf=1,ewr=7,adfd=00)
# print(dict2)
# # print(list1,list2,tuple1,set1,dict1)
# list3=[]
# list2.pop(-2)
# set2.remove("fdasf")
# del dict2["ewr"]
# # list2,tuple2,set2,
# print(dict2)

# list3=list2
# list3.insert(-1,6)
# set3=set2
# set3.add("fdasf")
# dict2["ewr"]=7
# dict3 = dict2
# print (list3)
# print (set3)
# print (dict3)

# a=6
# for a in range(1,6):
#     print(6)

# while True :
#     a=6
#     if a in range(1,6):
#         print("hellow")
#     else:
#         print("inside")
#         break
# a=3
# c=3
# if a==1:
#     print(a)
# elif c==3:
#     print(c)
# else:
#     breakpoint
# if "0":
#     print("a">"A")

# print(chr(95))

# if {1,}:
#     print("empty")
# else:
#     print("info")

# info = input("i")
# # print(info)
# # print(type(info))
# if info.isalnum():
#     print(type(info),info)

# 9.10
# from ccca import Restaurant
# restaurant = Restaurant("andy","noodles",7)
# restaurant.describe_restaurant()

# 9.11

# from ccca import Admin
# privileges = ["can add post", "can delete post", "can ban user"]
# admin = Admin("David", "wu", "admin", privileges)
# admin.show_privileges()

# 912
# from ccca import Admin

# privileges = ["can add post", "can delete post", "can ban user"]
# admin = Admin("David", "wu", "admin", privileges)
# admin.show_privileges()

# 9.13
# import random
# class Die:
#     def __init__(self):
#         self.sides = 20

#     def roll_die(self):
#         # self.sides= sides
#         a=0
#         while a != 10:
#             x = random.randint(1,self.sides)
#             print(x)
#             a+=1

# test=Die()
# test.roll_die()


# import random
# lottery_ticket = [1,5,3,4,7,2,8,5,9,3,"a","v","g","u","p"]
# a=0
# y=[]
# while a !=4:

#     x=random.choice(lottery_ticket)
#     print(x)
#     y.append(x)
#     a+=1
# print(y)
# print("If you can get these 4 electrice on lottery ticket, you win!")

# my_ticket = []
# while True:
#     c=0
#     c+=1
#     b=""
#     print(random.choice(lottery_ticket))
#     if b in y:
#         my_ticket.append(b)
#     if my_ticket == y:
#         print(c)
#         break


print(ord("A"))
print(ord("a"))
