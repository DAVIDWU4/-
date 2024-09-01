def print_contents(filename):
    file = open(filename,"r")
    text = file.read()
    file.close()
    print(text)


# def write_names(names):
#     file = open("output.txt","w")
#     mystring = ""
#     for name in names:
#         mystring += name+"\n"
#     string = mystring.strip("\n")
#     file.write(string)
#     file.close()

# write_names(['peter', 'dick', 'anna'])
# print_contents('output.txt')

# def write_reversed_file(filename):
#     file = open(filename,"r")
#     content = file.read()
#     file.close()

#     content1 = content[::-1]

#     file1 = open("output.txt", "w")
#     file1.write(content1)
#     file1.close()


# write_reversed_file("words2.txt")
# print_contents('output.txt')


# def combine_and_write(list1, list2):

#     string = ""
#     for index in range(len(list1)):
#         # string += f"{list1[index]} : {list2[index]}\n"
#         string += str(list1[index]) + " : " + str(list2[index])+"\n"
#     mystring = string.strip("\n")

#     file = open("output.txt","w")
#     file.write(mystring)
#     file.close()
# list1 = [2, 4, 5, 6, 8, 1]
# list2 = [123, 54, 58, 106, 87, 206]
# combine_and_write(list1, list2)
# print_contents('output.txt')


# def load_names(filename):
#     file = open(filename, "r")
#     content = file.read()
#     file.close()
#     names = content.split()
#     return names

# values = load_names("names.txt")
# print(values)

# def display_names(names_list):
#     for index in range(len(names_list)):
#         print(f"{index+1} : {names_list[index]}")

names_list = ['Abby', 'Bella', 'Charlotte', 'Daisy', 'Ella', 'Faith', 'Grace']
# display_names(names_list)

def remove_name(names_list, index):
    # count = 0
    # for a in index:
    #     print(f"'{names_list[a-count]}' is removed.")
    #     print(a)
    #     count+=1
    #     if count>0:
    #         print(names_list[a-count])
    #         del names_list[a-count]
    #     print(names_list)
    list1 = []
    for a in range(len(names_list)-1,-1,-1):
        if a in index:
            list1.append(names_list[a])
            del names_list[a]

    list1.reverse()

    for value in list1:
        print(f"'{value}' is removed.")
    print(names_list)

print(names_list)
remove_name(names_list, [3,6])


# def save_names(filename, names_list):
#     file = open(filename,"w")
#     string = ""
#     for text in names_list:
#         string += text+"\n"
#     mystring = string.strip("\n")
#     file.write(mystring)
#     file.close()

# save_names("a.txt", names_list)
