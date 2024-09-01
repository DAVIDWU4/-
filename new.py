# def display_message():
#     print ("function")
#     a = 1
#     print(1)
# display_message()

# print(1)
# def favorite_book(title):
#     print (f"One of my favorite book is {title}")

# favorite_book("Harry potter")

# def make_shirt(size="large",word = ""):
#     print (f"This T-shirt shoud be {size} size, writing on '{word}'")

# make_shirt( "small" ,"hey")

# def describe_city(city,land):
#     print (f"{city} is in {land}")

# describe_city("Reykjavik","Iceland")


# def city_country(where,city):
#     print (f"{where},{city}")

# city_country("Shanghai","China")







def make_album(albumname,singername,number=None):
    # b=""
    abc={}
    # if number == None:
    #     number =int(input ("input the number of albums: "))
    # abc={'number':number}
    # print ("if you want the loop stop input 'q': ")
    # while True :
        
    #     b = input ("input q to quit: ")
    #     if b == "q":
    #         break
        
    #     singername = input("input the name of the singer: ")
    #     albumname = input("input the album name of the album: ")
    abc[singername] = albumname
    #     if number != None:
    #         print (abc)
    #     else:
    #         print(abc)
    return abc



k = make_album(singername="sadjkh",albumname="sdrrtyyuu")
print(k)

