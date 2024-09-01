firstlist = [1]
secondlist = list((1,5))

print (secondlist)
print (range (0,5))

give = []
n = 'k'
while n != "q":
   n = input("输入q表示完成,输入数字：")
   if not n.isalpha():
       n = int(n)
       give.append(n)
print(give)
give.sort()
print (give)
even_lst = [x for x in give if x % 2 == 0]
odd_lst = [x for x in give if x % 2 != 0]
print (odd_lst)
newles = [0]

for a in odd_lst:
    
    print(a)
    newles.append(a)
    newles.append(0)
    
print (newles)    

gr = list({"live":"3","question":"7"})

print (gr)
getattr = list("hsdgfbhahjsdg")

print (getattr)

again = [list((1,5))]
again = [1,5,0]
again = [(1,5,6)]
again = [{1,4,5,6,4,3,5,2,4}]
again = [{"long":1,"strong":5}]

print (len(again),again)

a=1
apple = list([100,20,40,80] if  a<2 else 50)
banana = list(i for i in range (0,99))
print (banana)
print (apple)