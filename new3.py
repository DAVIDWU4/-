# class stack:
#     def __init__(self,orig_list,num):
#         self.orig_list = orig_list
#         self.num = num

#     def push(self):
#         self.orig_list.append(self.num)

#     def pull(self):
#         return self.orig_list.pop()

#     def peek(self):
#         return self.orig_list[-1]

#     def size(self):
#         c = len(self.orig_list)
#         return c

#     def is_empty(self):
#         if len(self.orig_list) == 0:
#             w = True
#         else:
#             w = False
#         return w


# orig_list = [1,3,5,7]
# num = int(input("enter: "))
# class1 = stack(orig_list,num)
# class1.push()
# print(class1.pull())
# print(class1.peek())
# print(class1.size())
# print(class1.is_empty())


# class queue:
#     def __init__(self, orig_list, num):
#         self.orig_list = orig_list
#         self.num = num

#     def enqueue(self):
#         self.orig_list.append(self.num)
#         print(self.orig_list)

#     def dequeue(self):
#         c = self.orig_list.pop(0)
#         print(self.orig_list)
#         return c

#     def peek(self):
#         return self.orig_list[-1]

#     def size(self):
#         return len(self.orig_list)

#     def is_empty(self):
#         if len(self.orig_list) == 0:
#             w = True
#         else:
#             w = False
#         return w

# orig_list = [1, 3, 5, 7]
# num = int(input("enter: "))
# lie = queue(orig_list[:],num)
# for a in range(3):
#     lie.enqueue()
#     print(orig_list)
# print(lie.dequeue())
# print(orig_list)
# print(lie.peek())
# print(lie.size())
# print(lie.is_empty())

import random
def random_function(point):
    num = []
    for a in range(point):
        # num.append(random.randint(1,100))
        num += [random.randint(1, 100)]
    num.sort()
    num.insert(0,1)
    num.append(100)
    print(num)
    # while True:
    #     length = len(num)
    #     if length == 1:
    #         return num
    #     middle = length//2
    #     if num[middle] < 20:
    #         del num[0:middle+1]
    #     else:
    #         del num[middle+1:length]

    start_index = 0
    end_index = len(num)-1
    while True:
        length = end_index-start_index+1
        if length == 2:
            if point-num[start_index]>num[end_index]-point:
                return end_index
            else:
                return start_index

        middle = length//2
        if num[middle] == point:
            return middle
        elif num[middle] < point:
            start_index = middle
        elif num[middle] > point:
            end_index = middle
point = int(input(": "))
print(random_function(point))
