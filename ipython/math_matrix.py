import numpy as np
import matplotlib.pyplot as plt
#
# # a = np.array([[2, 3, 4],
# #               [10, 20, 30]], dtype = np.float64)
# ####### 대각 행렬 Diagonal
# # a = np.array([1,2,3,4])
# # D1 = np.diag(a)
# # print(D1)
# #
# # b = np.random.randint(1, 10, 5)
# # D_2 = np.diag(b)
# # print(D_2)
# ###### 단위 행렬 Identity
# # I_3 = np.eye(3, 4)
# # print(I_3)
# ## 전치 행렬, Matrix transpose
a = np.array([[11, 12, 13, 14],
              [21, 22, 23, 24],
              [31, 32, 33, 34],
              [41, 42, 43, 44],
              [51, 52, 53, 54],
              [61, 62, 63, 64]], dtype = np.int64)
print("\n", a)
print("a_transpose \n", a.T)
######################## Matrix product
# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[1, 1],
#               [1, 2]])
# c = a*b
# print(np.matmul(a,b))



