# def get_statistics(numbers):
#     count = 0
#     sum = 0
#     for number in numbers:
#         if number >0:
#             sum += number
#             count += 1
#     average = sum / count
#     return (sum,round(average))

# a_list = [-2, 6, -3, -9, 20]
# print(get_statistics(a_list))


# def replace_a_value(a_tuple, index, new_value):
#     a_list = list(a_tuple)
#     a_list[index]= new_value
#     return tuple(a_list)

# tuple1 = ('one', 'two', 'three')
# tuple1 = replace_a_value(tuple1, 2, 'FOUR')
# print(tuple1)

# def create_tuples(list1, list2):
#     newlist = []
#     for a in range(len(list1)):
#         newlist.append((list1[a],list2[a]))
#     return newlist
# list_of_tuples = create_tuples(['one', 'two', 'three'], [1, 2, 3])
# print(list_of_tuples)

def replace_a_value(a_tuple, time): 
    return a_tuple+time



tuple1 = ('one', 'two', 'three')
tuple2 = ("c","b","x")
tuple1 = replace_a_value(tuple1,tuple2)
print(tuple1)
