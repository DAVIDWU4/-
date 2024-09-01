# human = {"first_name":"david","last_name":"wu","age":"18","city":"shanghai"}
# for v in human:
#     print (v,human[v])
#6.2
# like_number = {"david":8,"andy":5,"red":7,"green":9,"lucy":10}
# for a in like_number:
#     print (a,like_number[a])
# print (type(enumerate(like_number)))
# for v,x in enumerate(like_number):
#     print(v,x)

# print(type(like_number.items()))
# for k,v in like_number.items():
#     print(k,v)

# # 6.3+6.4  
# term = {"if":"judge","for":"circulation","range":"creat list","append":"add to the end","print":"print items",
#         "sort":"sort","del":"delete","key":"key of a value","remove":"delete a don't know place values","tuple":"tuple" }
# for x in term:
#     print (x,":",term[x])

# #6.5
# rivers = {"Nile" : "Egypt","Yellow river":"China", "Amazon river":"Brazil"}
# for river in rivers:
#     print (f"The {river} runs through {rivers[river]}.")

# for river in rivers:
#     print (river)

# for country in rivers.values():
#     print (country.title())

#6.6
# favorite_language = {
#     "jen":"python",
#     "sarah":"c",
#     "edward":"rust",
#     "phil":"python"
# }
# for name,language in favorite_language.items():
#     print (f"{name.title()}'s favorite language is {language.title()}.")
# test_people = ["jen","sarah","jay","payu"]
# for a in test_people:
#     if a in favorite_language:
#         print (a.title(),",thank you for comming to test.")
#     else :
#         print (a.title(),", please come to test.")


# #6.7
# human = {"first_name":"david","last_name":"wu","age":"18","city":"shanghai"}
# human1 = {"first_name":"cvay","last_name":"wu","age":"18","city":"shanghai"}
# human2 = {"first_name":"andy","last_name":"wu","age":"18","city":"shanghai"}
# people = [human,human1,human2]
# for v in people:
#     print (f'{v["first_name"].title()} {v["last_name"]},age:{v["age"]},live in {v["city"]}')

 
# 6.8
# pets=[{"taddy":"Andy"},{"papa":"lisa"},{"kitty":"caidy"}]
# for k in pets:
#     print(k)

# #6.9
# favorite_places = {"Andy":["Beijing","Shanghai","Mengo"],"Lisa":"Shanghai","Caidy":"Afghanistan"}
# for key,value in favorite_places.items():
#     print(f"{key}'s favorite places are",value)


# #6.10
# like_number = {"david":[8,5,48],"andy":[5,7,56],"red":[7,76,1],"green":[9,10,4],"lucy":[10,2,16]}

# for k,v in like_number.items():
#     print(k.title(),v)

# #6.11
# cities = {
#             "Shanghai":{"country":"China","population":"1.4 billion","fact":"very big"},
#             "Frolida":{"country":"America","population":"0.3 billion","fact":"crime city"},
#             "london":{"country":"England","population":"0.066 billion","fact":"the city of fog"}
#         }

# # for k,v in cities.items():
# #     print (f"{k}: {v}")
# cities["Berlin"]={"country":"Germany","population":"0.084 billion","fact":"the start of world war II"}
# for k,v in cities.items():
#     print (f"{k}: {v}")
    
# cities = dict(Berlin={"country":"Germany","population":"0.084 billion","fact":"the start of world war II"})

# for k,v in cities.items():
#     print (f"{k}: {v}")
    

city = dict(joe=12,david=13,sun=67)
print(city)

toy = {"diect","sanday","sahry"}
boy = {"sansus","dsf","rttrtee"}
print(dict(zip(boy,toy)))
del city["david"]
print(city)
city["david"] = ""
print(city)
