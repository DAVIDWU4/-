# # 7.1
# borrow_car = input ("What car do you want to borrow?")
# print (f"Let me see if I can find you a {borrow_car}.")

# #7.2
# people_eat = input ("how many people ")
# people_eat = int (people_eat)
# if people_eat > 8:
#     print ("no table for you.")
# else:
#     print ("we have table for you.")

# #7.3
# number = input("input a number: ")
# number = int (number)
# if number % 10 == 0 :
#     print ("This number is 10's integer multiples")
# else :
#     print ("This number isn't 10's integer multiples")

# # 7.4
# pizza = []
# x = ""
# while x != "q":
#     x = input("input what do you want to add on pizza: ")
#     pizza.append(x)
#     if  x == "q":
#         pizza.remove("q")
#     print(x)

# print (pizza)

# #7.5
# x=0
# while True:
#     age = []
#     age = input("how old are you: ")
#     if age == "q":
#         break
#     age=int(age)
#     if age <= 3:
#         print ("free")
#     elif 3< age <12:
#         print ("10$")
#     elif 12 <= age :
#         print ("15$")


# 7.6
# pizza = []
# active = True
# while active:
#     x = input("input what do you want to add on pizza: ")

#     if x =="q":
#         active = False
#     else:
#         pizza.append(x)
#         print(x)
# print (pizza)


# pizza = []

# while True:
#     x = input("input what do you want to add on pizza: ")
#     pizza.append(x)
#     print(x)
#     if x == "q":
#         pizza.remove("q")
#         break
# print (pizza)


# # 7.7
# while True :
#     print (1)

# # 7.8
# sandwich_orders = ["Black Forest Ham","Chicken & Bacon Ranch Melt","Cold Cut Combo","Italian B.M.T."]
# finaished_sandwich = []
# while sandwich_orders:
#     x=sandwich_orders.pop(0)
#     print(f"I made your {x} sandwich.")
#     finaished_sandwich.append(x)
# print(sandwich_orders)
# print(finaished_sandwich)

# # 7.9
# sandwich_orders = ["Black Forest Ham","pastrami","Chicken & Bacon Ranch Melt","pastrami","Cold Cut Combo","Italian B.M.T.","pastrami"]
# print ("pastrami is aready finished ")
# while sandwich_orders:
#     sandwich_orders.remove("pastrami")
#     if "pastrami" not in sandwich_orders:
#         break
# print (sandwich_orders)

# #7.10
# place = []
# while True:
#     place = input("If you could visit one place in the world,where would you go? ")
#     if place:
#         break
# print (place)

# def get_sum(value=None):
#     number = int(input("input a number:"))
#     # while True:
#     x=list(range (1,number+1))
#     x1 = sum(x)
#     print (x1)
#         # if x1:
#         #     break
#     return x1
# xa=get_sum()
# print (xa)

# def get_factorial(value=None):
#     number = int(input("input a number:"))
#     x=list(range (1,number+1))
#     power = 1
#     for n in x:
#         power = power* n

#     return(power)
# print (get_factorial())


# def list5(*list2):
#     list1 = list(list2)
#     list1.sort()
#     print (list1)
#     return list1

# x = int(input ("input number:"))
# y = int(input ("input number:"))
# z = int(input ("input number:"))
# c = int(input ("input number:"))
# v = int(input ("input number:"))

# print (list5(x,y,z,c,v))

# import statistics
# def list5(list2):
#     list1 = list2
#     print (min(list1))
#     print (max(list1))
#     print (statistics.mean(list1))
#     x = min(list1),max(list1),statistics.mean(list1)
#     return x


# x = int(input ("input number:"))
# y = int(input ("input number:"))
# z = int(input ("input number:"))
# c = int(input ("input number:"))
# v = int(input ("input number:"))
# list = [x,y,z,c,v]
# print (list5(list))


# print(min([3,9,0,1,5]))

# def sunday(a=None):
#     T = a
#     x=[]
#     for a in T:
#         if a =="T":
#             x.append("G")
#         elif a == "G":
#             x.append("T")
#     y="".join(x)
#     return y
# print (sunday("TTTGGTGTT"))


# def sss (a):
#     B=a[:]
#     B1=list(B)
#     print(a)
#     print(B1)
#     match=[]
#     for n,v in enumerate(B):
#         x = B1.pop(0)

#         if x in B1:
#             match.append((x,B.index(x)))
#     return match
# C = "dafhdqa"
# print(sss(C))

"""
        0~1之间的随机小数(float): random.random()
        a~b之间的随机小数(float): random.uniform(a, b)
        [a, b]之间的随机整数(int): random.randint(a, b)
        [a, b)之间的随机整数(int): random.randrange(a, b)
        随机地取一个值(等权): random.choice(lis),lis是一个列表
        对lis的原数据执行打乱操作, 本身无返回值, lis将被随机打散: random.shuffle(lis)
"""
# import random
# def jas(a=None):
#     x=y=z=c=v=b=n=i=u=p=q=0
#     while x < 1001:
#         ac=random.randint(0,10)
#         if ac == 1:
#             y+=1
#         elif ac == 2:
#             z+=1
#         elif ac == 3:
#             c+=1
#         elif ac == 4:
#             v+=1
#         elif ac == 5:
#             b+=1
#         elif ac == 6:
#             n+=1
#         elif ac == 7:
#             i+=1
#         elif ac == 8:
#             u+=1
#         elif ac == 9:
#             p+=1
#         elif ac == 10:
#             q+=1
#         Y=[f"1出现了{y}次,2出现了{z}次,3出现了{c}次,4出现了{v}次,5出现了{b}次,6出现了{n}次,7出现了{i}次,8出现了{u}次,9出现了{p}次,10出现了{q}次,"]
#         x+=1


#     return Y

# print(jas())

# import random
# def jas(a=None):
#     x=0
#     times=[0]*11

#     while x < 1001:
#         ac=random.randint(0,10)
#         if ac == 0:
#             times[0]+=1
#         elif ac == 1:
#             times[1]+=1
#         elif ac == 2:
#             times[2]+=1
#         elif ac == 3:
#             times[3]+=1
#         elif ac == 4:
#             times[4]+=1
#         elif ac == 5:
#             times[5]+=1
#         elif ac == 6:
#             times[6]+=1
#         elif ac == 7:
#             times[7]+=1
#         elif ac == 8:
#             times[9]+=1
#         elif ac == 9:
#             times[9]+=1
#         elif ac == 10:
#             times[10]+=1
#         Y=[f"0出现了{times[0]}次,1出现了{times[1]}次,2出现了{times[2]}次,3出现了{times[3]}次,4出现了{times[4]}次,5出现了{times[5]}次,6出现了{times[6]}次,7出现了{times[7]}次,8出现了{times[8]}次,9出现了{times[9]}次,10出现了{times[10]}次,"]
#         x+=1


#     return Y

# print(jas())


# def double_digit():

# # 9.1
# class restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(
#             f"{self.restaurant_name} is a good restaurant,it's type is {self.cuisine_type}."
#         )

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")


# Restaurant = restaurant("andy", "noodles")
# print(Restaurant.restaurant_name)
# print(Restaurant.cuisine_type)
# Restaurant.describe_restaurant()
# Restaurant.open_restaurant()


# 9.2
# class restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is a good restaurant")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")


# food = restaurant("andy", "noodles")
# food1 = restaurant("bayu", "noodles")
# food2 = restaurant("cici", "noodles")
# food.describe_restaurant()
# food.open_restaurant()
# food1.describe_restaurant()
# food2.describe_restaurant()
# print(food.restaurant_name)
# print(food.cuisine_type)
# print(food1.restaurant_name)
# print(food1.cuisine_type)
# print(food2.restaurant_name)
# print(food2.cuisine_type)


# # 9.3
# class user:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()

#     def describe_user(self):
#         # return self.first_name, self.last_name
#         print(self.first_name, self.last_name)

#     def greet_user(self):  # ??
#         print(f"Hi, {self.first_name} {self.last_name}")
#         # return (f"Hi, {self.first_name} {self.last_name}")


# user1 = user("andy", "no")
# user2 = user("bayu", "les")
# user3 = user("cici", "odl")
# user1.describe_user()
# user1.greet_user()
# user2.describe_user ()
# user2.greet_user()
# user3.describe_user ()
# user3.greet_user()
# print(user.describe_user(user1), user.greet_user(user1))  # ??
# print(user.describe_user(user2), user.greet_user(user2))  # ??
# print(user.describe_user(user3), user.greet_user(user3))  # ??


# # 9.4

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, number_served=0):
#         self.restaurant_name = restaurant_name.title()
#         self.cuisine_type = cuisine_type.title()
#         self.number_served = number_served

#     def describe_restaurant(self):
#         print(
#             f"{self.restaurant_name} is a good restaurant,it's type is {self.cuisine_type}."
#         )

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")

#     def set_number_served(self):
#         self.number_served = int(input("Please set number_served:"))  # ???
#         # print(self.number_served)

#     def increment_number_served(self, number_served):
#         self.number_served += number_served

#         print(f"{self.number_served} people eaten in this restraurant.")


#         # ???


# restaurant = Restaurant("andy", "noodles", 7)
# print(f"{restaurant.number_served} people maby every day.")
# # print(f"{self.increment_number_served(23)} people maby every day.")

# res = Restaurant("sada", ":ad", 5)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# res.describe_restaurant()
# res.open_restaurant()
# res.set_number_served()
# print(type(res.number_served))
# res.increment_number_served(9)


# # 9.5
class user:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name)

    def greet_user(self):
        print(self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        # print(self.login_attempts)  # ?

    def reset_login_attempts(self):
        self.login_attempts = 0
        # print(self.login_attempts)  # ?


# a = 0
# user1 = user("andy", "no")
# user1.describe_user()
# user1.greet_user()
# while a != 5:
#     user1.increment_login_attempts()
#     a += 1
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)


# # 9.6
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors

#     def show(self):
#         print(self.flavors)


# flavors = ["巧克力", "奶油", "抹茶", "草莓", "香草", "香芋", "咖啡", "树莓", "芒果", "绿茶"]

# iceCreamStand = IceCreamStand("andy", "noodles", flavors)
# iceCreamStand.show()


# 9.7

# class Admin(user):
#     def __init__(self, first_name, last_name, login_attempts, privileges):
#         super().__init__(first_name, last_name, login_attempts)
#         self.privileges = privileges

#     def show_privileges(self):
#         print(f"what Admin can do: {self.privileges}")


# privileges = ["can add post", "can delete post", "can ban user"]
# admin =Admin("David", "wu", "admin", privileges)
# admin.show_privileges()


# 9.8


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"what Admin can do:{self.privileges}")

class Admin(user):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges()

    def show_privileges(self):
        print(f"what Admin can do: {self.privileges}")

# privileges = ["can add post", "can delete post", "can ban user"]
# admin =Admin("David", "wu", "admin")
# admin.privileges.show_privileges()


# Admin = Privileges()
# Admin.show_privileges()


##9.9
class Car:
    "一次模拟汽车的简单尝试" ""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子,指出汽车的行驶里程"""
        print(f" This car has { self.odometer_reading} miles on it .")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电池的简单尝试"""

    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def upgrade_battery(self):
        """检查电池容量"""
        if self.battery_size != 65:
            self.battery_size = 65
        # return self.battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

# sample = Battery()
# sample.battery_size
# sample.upgrade_battery()
# sample.battery_size

class Admin1:
    class Admin(user):
        def __init__(self, first_name, last_name, login_attempts, privileges):
            super().__init__(first_name, last_name, login_attempts)
            self.privileges = privileges


        def show_privileges(self):
            print(f"what Admin can do: {self.privileges}")
        
    class ElectricCar(Car):
        """电动汽车的独特之处"""

        def __init__(self, make, model, year, battery_size=40):
            super().__init__(make, model, year)
            """初始化父类的属性"""
            self.battery = Battery()
            self.battery_size = battery_size

        def describe_battery(self):
            """打印一条描述电池容量的消息"""
            print(f"This car has a {self.battery_size}-kWh battery.")



# 9.9
# class Car:
#     "一次模拟汽车的简单尝试" ""

#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """返回格式规范的描述性名称"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """打印一个句子,指出汽车的行驶里程"""
#         print(f" This car has { self.odometer_reading} miles on it .")

#     def update_odometer(self, mileage):
#         """将里程表读数设置为给定的值"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """让里程表读数增加给定的量"""
#         self.odometer_reading += miles


# class Battery:
#     """一次模拟电动汽车电池的简单尝试"""

#     def __init__(self, battery_size=40):
#         """初始化电池的属性"""
#         self.battery_size = battery_size

#     def upgrade_battery(self):
#         """检查电池容量"""
#         if self.battery_size != 65:
#             self.battery_size = 65
#         # return self.battery_size

#     def describe_battery(self):
#         """打印一条描述电池容量的消息"""
#         print(f"This car has a {self.battery_size}-kWh battery")

#     def get_range(self):
#         """打印一条消息，指出电池的续航里程"""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225

#         print(f"This car can go about {range} miles on a full charge.")


# class ElectricCar(Car):
#     """电动汽车的独特之处"""

#     def __init__(self, make, model, year, battery_size=40):
#         super().__init__(make, model, year)
#         """初始化父类的属性"""
#         self.battery = Battery()
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """打印一条描述电池容量的消息"""
#         print(f"This car has a {self.battery_size}-kWh battery.")


# my_leaf = ElectricCar("nissan", "leaf", 2024)
# # print(my_leaf.get_descriptive_name())
# # my_leaf.describe_battery()
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()


class User:

    def __init__(self,first_name,last_name,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        return (self.first_name)

    def greet_user(self):
        return(self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    def reset_login_attempts(self,):
        self.login_attempts = 0
        return self.login_attempts
