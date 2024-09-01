# # 15.6
# import plotly.express as px
# from die import Die

# # 创建一个D6
# die = Die(num_sides=8)  # ？？两个D8
# die1 = Die(num_sides=8)
# results = []

# for roll_num in range(1000):
#     result = die.roll()
#     result1 = die1.roll()
#     results.append(result + result1)

# print(results)

# # 分析结果
# frequencies = []
# poss_results = range(2, die.num_sides * 2 + 1)  # ？？？
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)
# fig = px.line(x=poss_results, y=frequencies)
# fig = px.scatter(x=poss_results, y=frequencies)
# # fig = px.bar(x=poss_results, y=frequencies)
# fig.update_layout(xaxis_dtick=1)
# fig.show()


# # 15.7
# import plotly.express as px
# from die import Die

# # 创建一个D6
# die = Die()
# die1 = Die()
# die2 = Die()
# results = []

# for roll_num in range(100000):
#     result = die.roll()
#     result1 = die1.roll()
#     result2 = die2.roll()
#     results.append(result + result1 + result2)

# print(results)

# # 分析结果
# frequencies = []
# poss_results = range(3, die.num_sides * 3 + 1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

# # fig = px.line(x=poss_results, y=frequencies)
# fig = px.scatter(x=poss_results, y=frequencies)
# # fig = px.bar(x=poss_results, y=frequencies)
# fig.update_layout(xaxis_dtick=1)
# fig.show()


# 15.8
# import plotly.express as px
# import time
# from die import Die

# # 创建一个D6
# die = Die()
# die1 = Die()

# results = []
# time0 = time.time()
# for roll_num in range(100000000):
#     result = die.roll()
#     result1 = die1.roll()
#     results.append(result * result1)
# time1 = time.time()
# # print(results)

# print (time1-time0)
# time2 = time.time()
# # 分析结果
# frequencies = []
# poss_results = range(1, die.num_sides**2 + 1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)
# time3 = time.time()
# # print(frequencies)
# print (time3-time2)
# fig = px.bar(x=poss_results, y=frequencies)
# fig.update_layout(xaxis_dtick=1)
# fig.show()

# # 15.9
# import plotly.express as px
# from die import Die

# # 创建一个D6
# die = Die()
# die1 = Die()
# results = [die.roll() * die1.roll() for _ in range(100)]


# print(results)

# # 分析结果
# frequencies = []
# poss_results = range(3, 19)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

# fig = px.bar(x=poss_results, y=frequencies)
# fig.show()


import matplotlib.pyplot as plt
import math
x = list(range (-10, 10,1))
x1 = list(range(-4, 101, 1))
y = [a**2-4 for a in x]
y1 = [math.sqrt(a+4) for a in x1]
plt.plot(x, y, label="nomal")
plt.plot(x1, y1, label="inverse")
plt.show()
