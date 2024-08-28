import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-4, 4, 100)
# def polynomial(x, n):
#     y = x**n
#     return y
#
# y1 = polynomial(x,1)
# y2 = polynomial(x,2)
# y3 = polynomial(x,3)
# plt.plot(x, y1, label = "Y = X")
# plt.plot(x, y2, label = "y = x^2")
# plt.plot(x, y3, label = "y = x^3")
# plt.plot(x, polynomial(x, 4), label = " y = x^3")
# plt.ylim(-2, 2)
# plt.xlim(-2, 2)
# plt.legend()
# plt.grid(linestyle = ":")
# plt.show()
#-------------------------------------------------------------
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# # print(x)
# sin_x = np.sin(x)
# cos_x = np.cos(x)
# tan_x = np.tan(x)
#
# plt.figure(figsize= (12, 5))
# # plt.plot(x, sin_x, label = "sin(x)")
# # plt.plot(x, cos_x, label = "cos(x)")
# plt.plot(x, tan_x, label = "tan(x)")
# plt.vlines(0, -1, 1, color = 'r')
# plt.hlines(0, -2*np.pi, 2*np.pi, color = 'b')
# plt.ylim(-1,1)
# plt.xlim(-2*np.pi, 2*np.pi)
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels =
#                         ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.legend()
# plt.grid(linestyle = ":")
# plt.show()
#==============================================================
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
#
# sin_x = np.sin(x)
# cos_x = np.cos(x)
# tan_x = np.tan(x)
#
# y_list = [sin_x, cos_x, tan_x]
# y_label = ["sin(x)", "cos(x)", "tan(x)"]
# color_list = ["blue", "green", "red"]
# fig, ax = plt.subplots(3, 1, figsize = (12, 10))
# for i in range(3):
#     ax[i].plot(x, y_list[i], label = y_label[i], c = color_list[i])
#     ax[i].set_ylim(-1, 1)
#     ax[i].grid(linestyle = ':')
#     ax[i].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels =
#                          ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.show()
#===============================================================
# (1) y - b = sin(x - a)의 그래프는 y = sin(x)의 그래프를 x축으로 a, y축으로 b만큼 평행 이동한 것이다.
# (1) y = sin(x - a) + b의 그래프는 y = sin(x)의 그래프를 x축으로 a, y축으로 b만큼 평행 이동한 것이다.
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.sin(x)
# y1 = np.sin(x - 2*np.pi) + 1
# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = 'sin(x)')
# plt.plot(x, y1, label = 'sin(x - pi) + 1')
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend()
# plt.show()
# (2) y = -sin(x)의 그래프는 y - sin(x)의 그래프를 x축을 중심으로 선대칭이다
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.tan(x)
# y1 = -np.tan(x)
# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = 'tan(x)')
# plt.plot(x, y1, label = '-tan(x)', linestyle = ':')
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend()
# plt.show()
# (3) y = a sin(x)의 그래프는 y = sin(x)의 함숫값을 a배한 것이다
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.cos(x)
# y1 = 2*np.cos(x)
# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = 'cos(x)')
# plt.plot(x, y1, label = '-cos(x)', color = 'red')
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend()
# plt.show()
#(4) y = sin(ax)의 그래프는 y = sin(x) 와 모양은 같고 주기가 2pi/ |a|인 그래프이다
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.cos(x)
# y1 = np.cos(2*x)
# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = 'cos(x)')
# plt.plot(x, y1, label = '-cos(x)', color = 'red')
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend()
# plt.show()
#=================================================예제
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.sin(x - np.pi/2)
# y1 = np.sin(x - np.pi/2) + 1
# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = 'sin(x)')
# plt.plot(x, y1, label = '-sin(x)', color = 'red')
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend()
# plt.show()
#=================================================예제2
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 2*np.sin(x)
y1 = 2*np.sin(x - np.pi/2) + 1
plt.figure(figsize = (12, 5))
plt.plot(x, y, label = 'sin(x)')
plt.plot(x, y1, label = '-sin(x)', color = 'red')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend()
plt.show()
#================================================에제3
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(2*x)
y1 = 2*np.sin(2*(x - np.pi/2)) + 1
plt.figure(figsize = (12, 5))
plt.plot(x, y, label = 'sin(x)')
plt.plot(x, y1, label = '-sin(x)', color = 'red')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend()
plt.show()
#================================================에제4
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x - np.pi/2)
y1 = -np.cos(x) + 1
y2 = np.cos(2*x + np.pi)
plt.figure(figsize = (12, 5))
plt.plot(x, y, label = 'sin(x)')
plt.plot(x, y1, label = '-sin(x)', color = 'red')
plt.plot(x, y2, label = '-sin(x)', color = 'black')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend()
plt.show()
