import numpy as np
import matplotlib.pyplot as plt

# v1 = np.array([1, 1])
# v2 = np.array([-2, -1])
#
# plt.quiver(0, 0, v1[0], v1[1], angles = 'xy', scale_units = "xy"
#            , scale = 1
#            , color = "r")
# plt.quiver(0, 0, v2[0], v2[1], angles = 'xy', scale_units = "xy"
#            , scale = 1
#            , color = "b")
# plt.xlim(-3, 3)
# plt.ylim(-3, 3)
# plt.grid(linestyle = ':')
# plt.show()
#=====================================================
# v1 = np.array([[1, 1],
#               [-2, 2],
#               [4, -7]])
# origin = np.array([[0,0,0],
#                    [0,0,0]])
# plt.quiver(*origin, v1[:, 0], v1[:, 1], angles = 'xy',
#            scale_units = 'xy',
#            scale = 1,
#            color = ['r', 'g', 'c'])
# plt.grid(linestyle = ":")
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# plt.show()
#===========================================================
# def projection_vec(base_vec, proj_vec):
#     scalar = np.inner(base_vec, proj_vec)/np.linalg.norm(base_vec)**2
#     p_vec = scalar*base_vec
#     plt.quiver(0,0,base_vec[0], base_vec[1], angles = 'xy',
#                scale_units = 'xy', scale = 1, color = 'r',
#                label = 'Base Vector')
#     plt.quiver(0, 0, proj_vec[0], proj_vec[1], angles='xy',
#                scale_units='xy', scale=1, color='b',
#                label='Target Vector')
#     plt.quiver(0, 0, p_vec[0], p_vec[1], angles='xy',
#                scale_units='xy', scale=1, color='k',
#                label='Projected Vector')
#     plt.xlim(-8, 8)
#     plt.ylim(-8, 8)
#     plt.grid(linestyle = ":")
#     plt.legend()
#     plt.show()
# projection_vec(np.array([-2, 1]), np.array([-6,4]))


