# def print_dictionary_in_order(a_dict):
#     dictionary = dict(sorted(a_dict.items()))
#     for key in dictionary:
#         dictionary[key] = sorted(dictionary[key])
#     for keys in dictionary:
#         print(f"{keys} :{dictionary[keys]}")
#     return dictionary
# a_dict = {3: [5, 3, 7], 7: [6, 2], 2: [2, 1], 8: [-3, 9]}
# print_dictionary_in_order(a_dict)


# def create_2d_square_numbers_list(n):
#     result = []
#     for num in range(1,n+1):
#         result.append([num]*n)
#     return result
# print(create_2d_square_numbers_list(4))


# def create_2d_list(word):
#     result = []
#     for a in word:
#         list1 = []
#         for num in word:
#             list1.append(num)
#         result.append(list1)
#     return result
# print(create_2d_list('elephant'))

# def get_row_sum(list_of_lists, row_index):
#     for a in range(len(list_of_lists)):
#         if a == row_index:
#             return sum(list_of_lists[a])

# nums = [[3], [2, 4, 6], [3, 6], [3, 6, 9, 12]]
# print(get_row_sum(nums, 2))

# def get_column_sum(list_of_lists, column_index):
#     sum1 = 0
#     for a in list_of_lists:
#         sum1 += a[column_index]
#     return sum1


# nums = [[3], [2, 4, 6], [3, 6], [3, 6, 9, 12]]
# print(get_column_sum(nums, 0))

def get_accumulated_sum(list_of_lists):
    sum_list = 0
    for list in list_of_lists:
        sum_list += sum(list)
    return sum_list

a_list = [[1, 2, 3], [4, 5], [2, 3]]
print(get_accumulated_sum(a_list))

def get_list_of_sums(list_of_tuples):
    total = []
    for list1 in list_of_tuples:
        newlist = list(list1)
        total.append(sum(newlist))
    return total

a_list = [(1, 2, 3), (4, 5), (2, 3)]
print(get_list_of_sums(a_list))


# def double_up(list_of_lists):
#     for list1 in range(len(list_of_lists)):
#         for num in range(len(list_of_lists[list1])):
#             list_of_lists[list1][num] = list_of_lists[list1][num]*2


# a_list = [[1, 2, 3], [4, 5], [2, 3]]
# double_up(a_list)
# print(a_list)
