number = 5
first = 6


def func(para):
    doublenum = para * 2
    sumnum = number + 2
    # number = 3
    return doublenum, sumnum


# x,y=(4,10)
X = Y = (4, 1)
x, y = func(first)
print(func(first))
print(f"Double_number={x},sum_number={y}")


# def func2(para):
#     second=16
#     multiple=para(second)
#     return multiple
# v,s=func2(func)
# print(f"Double_number={v},sum_number={s}")


# def funcOut(para):
#     second=16
#     def funcIn(second):
#         multiple=para(second)
#         return multiple
#     return funcIn
# v,s=funcOut(func)
# print(f"Double_number={v},sum_number={s}")
