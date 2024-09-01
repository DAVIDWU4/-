# def english_to_italian(translation_dict, english_word):
#     if english_word in translation_dict:
#         return translation_dict[english_word]
#     return 'N/A'
# english_italian = {"yes":"si","bye":"ciao","no":"no","maybe":"forse","thank you":"grazie"}
# print(english_to_italian(english_italian,'yes'))
# print(english_to_italian(english_italian,'sorry'))

# def update_or_add (a_dict, key, value):
#     if key in a_dict:
#         old_value = a_dict[key]
#         print(old_value,"is replaced by", value)
#         a_dict[key] = value
#     else:
#         a_dict[key] = value
#         print("A new pair is added ->", key, ":", a_dict[key])
#     print(a_dict)

# fruit = {'a':'apple','b':'banana','g':'grape'}
# update_or_add(fruit, 'a','apricot')
# fruit = {"a": "apricot", "b": "banana", "g": "grape"}
# update_or_add(fruit, "f", "feojoa")


def delete_or_add (a_dict, key, value):
    if key in a_dict:
        print(f"{a_dict[key]} is deleted.")
        del a_dict[key]

    else:
        a_dict[key] = value
        print("A new pair is added ->", key, ":", a_dict[key])
    print(a_dict)

# fruit = {"a": "apple", "b": "banana", "g": "grape"}
# delete_or_add(fruit, "a", "apricot")
fruit = {"a": "apricot", "b": "banana", "g": "grape"}
print(fruit)
delete_or_add(fruit, "f", "feojoa")
print(fruit,"f")

# def diction(a_dict,key):
#     if key in a_dict:
#         del a_dict[key]
#         print(a_dict)
#     else:
#         print("this key is not in a_dict")
# diction(fruit, "c")


# def create_contacts_dictionary(names, numbers):
#     contacts_dict = {}
#     for index in range(len(names)):
#         contacts_dict[ names[index] ] = numbers[index]
#     return contacts_dict
# names = ["Jill", "James"]
# numbers = [3456, 7654]
# print(create_contacts_dictionary(names, numbers))
