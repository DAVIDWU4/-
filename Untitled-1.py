# def get_discount(price, rate):
#     money = price*(rate/100)
#     return round(money, 2)


# discount_message = "Discount: $" + str(get_discount(234, 5))
# print(discount_message)
# discount_message = "Discount: $" + str(get_discount(125, 15))
# print(discount_message)


# def get_discount_message(discount, rate):
#     return(f"{rate}% Discount: ${discount}")


# discount_message = get_discount_message(11.7, 5)
# print(discount_message)
# discount_message= get_discount_message(98.55, 15)
# print(discount_message)

# def get_discount(amount, rate):
# #code from slide 10
#     money = amount*(rate/100)
#     return round(money, 2)

# def get_discount_message(discount, rate):
# #code from slide 11
#     return(f"{rate}% Discount: ${discount}")

# def print_docket(price, rate):
#     print(f"Original price ${price}")
#     print(get_discount_message(get_discount(price, rate), rate))
#     print(f"Price ${price - get_discount(price, rate)}")

# print_docket(234, 5)
# print()
# print_docket(657, 15)

# def main():
#     price = int(input("Please enter the price of the item: $"))
#     rate = int(input("Please enter the discount rate: "))
#     print_docket(price, rate)

# def get_discount(amount, rate):
# #code from slide 10
#     money = amount*(rate/100)
#     return round(money, 2)
# def get_discount_message(discount, rate):
# #code from slide 11
#     return(f"{rate}% Discount: ${discount}")
# def print_docket(price, rate):
# #code from slide 12
#     print(f"Original price ${price}")
#     print(get_discount_message(get_discount(price, rate), rate))
#     print(f"Price ${price - get_discount(price, rate)}")
# main()
