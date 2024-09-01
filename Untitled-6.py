# def print_dictionary(a_dict):
#     sorted_dict = dict(sorted(a_dict.items()))
#     for key in sorted_dict:
#         print(f"{key}: {sorted_dict[key]}")
# a_dict = {3:[5,3,7],7:[6,2],2:[2,1],8:[-3,9]}
# print_dictionary(a_dict)


# def create_words_count_dictionary(words):
#     word_count_dict = {}
#     for word in words:
#         if word in word_count_dict:
#             word_count_dict[word] += 1
#         else:
#             word_count_dict[word] = 1
#     return word_count_dict

# words = ['word','hello','world','hello']
# print(create_words_count_dictionary(words))

def create_abc_dictionary(words):
    dic = {'a':[],'b':[],'c':[]}
    for word in words:
        first_letter = word[0]
        if first_letter in dic:
            dic[first_letter].append(word)
    return dic

words = ["avocado", "blackcurrant", "coconut", "blackberries", "cantaloupe"]
print(create_abc_dictionary(words))

# def create_alphabet_dictionary(words):
#     dic = {}
#     for word in words:
#         first_letter = word[0]
#         if first_letter not in dic.keys():
#             dic[first_letter] = [word]
#         else:
#             dic[first_letter].append(word)
#     return dic

# words = ['word','user','apple','hello']
# print(create_alphabet_dictionary(words))
