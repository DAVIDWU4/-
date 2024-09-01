for num1 in range(1,1001):

    flag = 1
    for num in range(2,num1-1):
        if num1 % num==0:
            flag = 0
            break

    if flag == 1 and num1 != 1:
        print(num1)