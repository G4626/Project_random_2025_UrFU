# В v13 ПЕРЕДЕЛАЙ ПОД ПРИБЛИЖЕНИЕ ДО err=1%
# v12.5 , ИСКЛЮЧИТЕЛЬНО N=6, задаётся err а не MCS_total
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math

r = 1
N = 6
#MCS_total = 100
err_ = 0.01
F_max = 22.970562685225847 #

dots_coord = [[0, 0, r] for i in range(N)]
#dist_partial = [0 for i in range(N)]

pi = np.pi
cos = np.cos
sin = np.sin

jump_dist_max = pi/12 # НЕ БОЛЕЕ pi , ТК НЕ ИМЕЕТ СМЫСЛА

def matrix_multiplication(A, B):
	res = [[0 for i in range(len(B[0]))]for j in range(len(A))]
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				res[i][j] += A[i][k] * B[k][j]
	return res

data_ = open('project_data_r1_N6_err0.01_j12_4.txt', 'w') # СЮДА ПИХАТЬ ИМЯ ФАЙЛА_ВЫВОДА

def norm_(xyz):
	l = (xyz[0]**2+xyz[1]**2+xyz[2]**2)**0.5
	xyz[0] *= (r/l)
	xyz[1] *= (r/l)
	xyz[2] *= (r/l)
	return xyz

def dist_sum(coords_i):
	s = 0
	for j in range(len(coords_i)):
		for k in range(len(coords_i)):
			s += ((coords_i[j][0]-coords_i[k][0])**2+(coords_i[j][1]-coords_i[k][1])**2+(coords_i[j][2]-coords_i[k][2])**2)**0.5
	return s/2

chosen_dot = 0
MCS_i = 0
F = 0
i = 0
while (1-F/F_max) > err_:
	chosen_xyz = dots_coord[chosen_dot]
	jump_axis_xyz = dots_coord[chosen_dot]
	# генерируем коорд прыжка относительно оси
	xi  = random.random()
	eta = random.random()
	theta_2 = np.arccos(cos(jump_dist_max)+eta*(1-cos(jump_dist_max)))
	phi_2 = 2*pi*xi
	new_xyz_relative = [sin(theta_2)*cos(phi_2), sin(theta_2)*sin(phi_2), cos(theta_2)]
	# преобразуем коорд прыжка в абсолютные(относительно базисов)
	if chosen_xyz[2] != r:
		theta_1 = np.arccos(chosen_xyz[2]/r)
		phi_1 = np.arccos(chosen_xyz[0]/((r**2-chosen_xyz[2]**2)**0.5))
		if chosen_xyz[1]/(r*sin(theta_1)) < 0:
			phi_1 += pi
		U = [ [cos(theta_1)*cos(phi_1), -sin(phi_1)*cos(theta_1), -sin(theta_1)],
		[-sin(phi_1), cos(phi_1), 0],
		[cos(phi_1)*sin(theta_1), sin(phi_1)*sin(theta_1), cos(theta_1)] ]
		new_xyz = matrix_multiplication([new_xyz_relative], U)[0]
	else:
		new_xyz = new_xyz_relative
	new_xyz = norm_(new_xyz) # нормировка
	# перерасчёт расстояния (пока по прямой)
	coords_new = dots_coord[:chosen_dot]+[new_xyz]+dots_coord[chosen_dot+1:]
	F_new = dist_sum(coords_new)
	if F_new>F:
		F = F_new
		dots_coord[chosen_dot] = new_xyz
		print("+++++++++++++++++++++++++++++", i, MCS_i,  chosen_dot, dots_coord, F) #
		data_.write(str(i)+ ' ' + str(MCS_i) + ' ' + str(F) + " " + str(dots_coord) + "\n")
	chosen_dot += 1
	if chosen_dot == N:
		chosen_dot = 0
		MCS_i+=1
	i += 1


# конечный дебажный вывод
for i in range(N):
	print(i, dots_coord[i])
print(F)

data_.close()

'''
# тут отрисовка
theta, phi = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(theta)*cos(phi)
y = r*sin(theta)*sin(phi)
z = r*cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='c', alpha=0.6, linewidth=0)

for dot_ in dots_coord:
	ax.scatter(dot_[0],dot_[1],dot_[2],color="r",s=20)

for i in range(N):
	for j in range(i+1, N):
		X_ = [dots_coord[i][0], dots_coord[j][0]]
		Y_ = [dots_coord[i][1], dots_coord[j][1]]
		Z_ = [dots_coord[i][2], dots_coord[j][2]]
		#print('----', X_, Y_, Z_)
		plt.plot(X_, Y_, Z_, color="r")

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
plt.tight_layout()
plt.show()
'''
