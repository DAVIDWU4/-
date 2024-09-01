# name = "david"
# age = 19
# print("introduce your self my name is:{2:*^10}, my age is:{1:*>10},else {0:*<10}".format(name,age,"fy"))
# print("introduce your self {:^11}".format(name))
# print("introduce your self {:<11}".format(name))
# print("introduce your self {:11}".format(name))

# print("introduce your self {:a>11}".format(name))
# print("introduce your self {:a^11}".format(name))
# print("introduce your self {:s<11}".format(name))
# print("introduce your self {:a<11}".format(name),end = "")
# print("ok")


# num = [1,7,3,7,9]
# c = sum(num)
# result = c/len(num)
# print(f"origin list:{num}, average is {result:10}, max is {max(num):10}, min is {min(num):10}")
# print("origin list:{}, average is {:10}, max is {:10}, min is {:10}".format(num,result,max(num),min(num)))


# num1 = int(input("num: "))
# print(True if num1 % 8 == 0 else 'else' if num1 % 7 ==0 else False)

# def dav(name,age = 18,gender = "male"):
#     print(name)
#     print(age)
#     print(gender)

# dav(gender = "female",name = "david")

# even_list=[odd**2 for odd in range(51) if odd%2 == 0]
# print(even_list)
# all_list = [odd**2 if odd % 2 == 0 else odd for odd in range(51) ]
# print(all_list)


list1 = [1,3,5]
list1 *= 2 
print(list1)