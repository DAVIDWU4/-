# def get_contents_length(filename):
#     file = open(filename, "r")
#     contents = file.read()
#     file.close()
#     newstring = contents.split("\n")
#     newcontents = "".join(newstring)
#     count = len(newcontents)
#     return count

# print(get_contents_length('baby_names.txt'))


# def get_contents_length(filename):
#     file = open(filename, "r")
#     contents = file.read()
#     file.close()
#     newcontents = contents.replace("\n","")
#     count = len(newcontents)
#     return count


# print(get_contents_length("baby_names.txt"))


# def read_names(filename):
#     file = open(filename, "r")
#     contents = file.read()
#     file.close()
#     new = contents.split()
#     return new

# print(read_names('baby_names.txt'))

# def read_n_lines(filename, n):
#     file = open(filename,"r")
#     for a in range(n):
#         contents = file.readline()
#         contents = contents.strip("\n")
#         print(contents)
#     file.close()
    

# read_n_lines('summer.txt', 0)

# def print_line_number(filename):
#     file = open(filename,"r")
#     contents = file.read()
#     file.close()
#     contents = contents.strip("\n")
#     newline = contents.split("\n")
#     count = 1
#     for line in newline:
#         print(f"{count} {line}")
#         count += 1

# print_line_number('sentences.txt')


# def get_first_last (filename):
#     file = open(filename,"r")
#     contents = file.read()
#     file.close()
#     contents = contents.strip("\n")
#     # return f"{contents[0]}{contents[-1]}"
#     return contents[0]+ contents[-1]

# print(get_first_last('sentences.txt'))
# print(get_first_last('summer.txt'))

# def get_first_last_per_line(filename):
#     file = open(filename,"r")
#     contents = file.readlines()
#     file.close()
#     list1 = []
#     for a in contents:
#         a = a.strip("\n") 
#         list1.append(a[0]+a[-1])
#     return list1

# print(get_first_last_per_line('sentences.txt'))

# def read_integers(filename):
#     file = open(filename,"r")
#     content = file.read()
#     file.close()

#     newlist = content.split()
#     number = []
#     for a in newlist:
#         if not a.isalpha():
#             a = int(a)
#             number.append(a)
#     return number
# print(read_integers('numbers2.txt')) 