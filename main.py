import readdata as rd
import numpy as np
import math
import getrad
import Model


data = rd.openreadtxt('D:\\大地形变测量学\\第二次作业说明\\青藏高原GPS数据\\gps_data.txt.txt')

#  地球半径值（m）
r0 = 6371393000
#  把数据读入
lon = []
lat = []
Ve = []
Vn = []
xigmae = []
xigman = []
name = []
result = []
for i in range(len(data)):
    lon.append(getrad.getrad(float(data[i][0])))
    lat.append(getrad.getrad(float(data[i][1])))
    Ve.append(float(data[i][2]))
    Vn.append(float(data[i][3]))
    xigmae.append(float(data[i][4]))
    xigman.append(float(data[i][5]))
    name.append(data[i][6])

# 计算B矩阵的部分值
avg_L = sum(lon) / len(lon)
avg_B = sum(lat) / len(lat)
delta_L = np.array(lon) - avg_L
delta_B = np.array(lat) - avg_B

# ModeL
L = np.empty((2 * len(data), 1))
B = []
for i in range(5):
    B.append(np.empty((2 * len(data), 6)))
    result.append(np.empty((2 * len(data), 6)))

X0 = np.empty((6, 1))
D = np.empty((2 * len(data), 2 * len(data)))
for i in range(len(data)):
    L[2 * i, 0] = Ve[i]
    L[2 * i + 1, 0] = Vn[i]
    B[0][i * 2] = [1, -math.sin(avg_B) * delta_L[i], r0 * math.cos(avg_B) * delta_L[i], 0, 0.5 * r0 * delta_B[i],
                   r0 * delta_B[i]]
    B[0][2 * i + 1] = [-math.sin(avg_B) * delta_L[i], 1, 0,
                       r0 * delta_B[i], 0.5 * r0 * math.cos(avg_B) * delta_L[i], -r0 * math.cos(avg_B) * delta_L[i]]
    B[1][i * 2] = [1, 0, r0 * math.cos(avg_B) * delta_L[i], 0, 0.5 * r0 * delta_B[i], r0 * delta_B[i]]
    B[1][i * 2 + 1] = [0, 1, 0, r0 * delta_B[i], 0.5 * r0 * math.cos(avg_B) * delta_L[i],
                       -r0 * math.cos(avg_B) * delta_L[i]]
    D[2 * i, 2 * i] = 1 / (xigmae[i] * xigmae[i])
    D[2 * i + 1, 2 * i + 1] = 1 / (xigman[i] * xigman[i])

for i in range(2):
    result[i] = Model.Model1(L, B[i], D)

# Save the result to a text file
rd.save_matrices_to_text(result, 'result_matrices.txt')
