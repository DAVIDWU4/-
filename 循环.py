cyclenumber = 1
list1 = []


# creat a new list and told user input cycle 8 times  
while cyclenumber <=8: 
    a = input ("请输入8次,每次输入一个数字: ")
    list1.append(a)
    cyclenumber += 1
 
tuple1 = tuple(list1) #设定 tuple1 元组

dictionaries1 = {r: len(r) for r in list1}

gather1 = set (list1)

#循环 list1 里的每一个值
for b in list1:
    print (b)  
    

# cycle tuple1 every numbers
for c in tuple1: 
    print (c)   

for d in dictionaries1:
    print (d)

for e in gather1:
    print (e)