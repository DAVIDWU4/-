# def make_album(albumname,singername,number=None):
#     # b=""
#     abc={}
#     # if number == None:
#         # number =int(input ("input the number of albums: "))
#     abc={'number':number}
#     print ("if you want the loop stop input 'q': ")
#     while True :
        
#         b = input ("input q to quit: ")
#         if b == "q":
#             break
        
#         singername = input("input the name of the singer: ")
#         albumname = input("input the album name of the album: ")
#         abc[singername] = albumname
#     #     if number != None:
#     #         print (abc)
#     #     else:
#     #         print(abc)
#     return abc


# k = make_album(singername="sadjkh",albumname="sdrrtyyuu",number=3)
# while True :
        
#         b = input ("input q to quit: ")
#         if b == "q":
#             break
        
#         singername = input("input the name of the singer: ")
#         albumname = input("input the album name of the album: ")
#         abc[singername] = albumname


# print(k)


# def show_message(apple):
#     for n in apple:
#         print (n)
    


# acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
# show_message(acc)



# def show_message(apple,sent_message):
#     while apple:
#         save = apple.pop(0)
#         print (save)
#         sent_message.append(save)
#         send_message(apple,sent_message)

# def send_message(apple,sent_message):
#     print (f"apple: {apple}")
#     print ("sent message: ",sent_message)
    

# sent_message = []
# acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
# print (acc)
# show_message(acc,sent_message)



def show_message(apple):
    sent_message = []
    while apple:
        save = apple.pop(0)
        print (save)
        sent_message.append(save)
        print (f"apple: {apple}")
        print ("sent message: ",sent_message)



# acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]

# show_message(acc[:])
# print(f"acc: {acc}")



# def sandwich(*sandwich):
#     print(type(sandwich))
#     print(sandwich)
#     # 三明治每层材料，循环每次调用不一样
#     for n in sandwich:
#         print (f"\nIn this sandwich we will use material: {n} ")

# w = 0
# happy=[]*3
# print(len(happy))
# while True:
#     nat=input("what do you want to put in your sandwich?\n:")
#     if nat=='q':
#         break
#     happy.append(nat)

# sandwich(happy[0],happy[1],happy[2])





# def car(creater,car_type,**car):
#     car["creater"] = creater
#     car["car_type"] = car_type
#     return car


# cars= car("大众","T管", color = "red", add = "front")

# print (cars)





def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('David','wu',
                             location = 'shanghai',
                             field = 'physics')
print (user_profile)

