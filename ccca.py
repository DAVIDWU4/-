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

# class DaDa:
from a import *
class Admin(User):
    def __init__(self,first_name,last_name,login_attempts,privileges):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        print(f"what Admin can do:{self.privileges}")


