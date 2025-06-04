# ПЕРЕПИШИ v3 ПОД НОВЫЙ ВЫВОД + КОМПИЛЯЦИЮ ГРАФИКОВ ДОБАВЬ
# ВРОДЕ РАБОТАЕТ, НО БЕЗ КОМПИЛЯЦИИ ПОКА....
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math
import re
'''
data_ = open('project_data_3_r1_N101_d1000_j1_test___1.txt', 'r')
data_r = data_.read().splitlines()
'''
r = 1
N = 5

D = []
def reading_pocess():
	for step_ in data_r:
		D_i_unprocessed = step_.split()
		#print("+",D_i_unprocessed)
		D_i = [float(D_i_unprocessed[0]), float(D_i_unprocessed[1]), float(D_i_unprocessed[2]), []]
		X = []
		for i in range(3, len(D_i_unprocessed)):
			#print("++++++++++++++++++", D_i_unprocessed[i])
			X_i = float(re.sub(r'[^0-9.e-]+', r'', D_i_unprocessed[i]))
			X.append(X_i)
			#print("+++++++++++++++++", X_i, X)
			if ']' in D_i_unprocessed[i]:
				D_i[-1].append(X)
				X = []
		#print("++",D_i) #
		D.append(D_i)

def graf_():
	x, y = [], []
	for i in D:
		x.append(i[1])
		#x.append(np.log(i[0])) #
		y.append(i[2])
	plt.plot(x, y)
	plt.scatter(x, y, s=2, color="r")
	plt.xlabel('MCS') 
	plt.ylabel('F')
	plt.show()

def sphere_drawer():
	pi = np.pi
	cos = np.cos
	sin = np.sin
	phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
	x = r*sin(phi)*cos(theta)
	y = r*sin(phi)*sin(theta)
	z = r*cos(phi) 
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='c', alpha=0.6, linewidth=0)
	
	xyz = D[-1][-1]
	for dot_ in xyz:
		ax.scatter(dot_[0],dot_[1],dot_[2],color="r",s=20)
	#''' #
	for i in range(len(xyz)):
		for j in range(i+1, len(xyz)):
			X_ = [xyz[i][0], xyz[j][0]]
			Y_ = [xyz[i][1], xyz[j][1]]
			Z_ = [xyz[i][2], xyz[j][2]]
			plt.plot(X_, Y_, Z_, color="r")
	#''' #
	ax.set_xlim([-1,1])
	ax.set_ylim([-1,1])
	ax.set_zlim([-1,1])
	ax.set_aspect("equal")
	plt.tight_layout()
	plt.show()

def distribution_check():
	xyz = D[-1][-1]
	Z = []
	PHI = []
	for c in xyz:
		if abs(c[2]) != r:
			Z.append(c[2])
			phi_i = np.arccos(c[0]/((r**2-c[2]**2)**0.5))
			if c[1] < 0:
				phi_i += np.pi
			PHI.append(phi_i)
	fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
	axs[0].hist(Z, bins=N)
	axs[0].set_ylabel('N')
	axs[0].set_xlabel('Z');
	axs[1].hist(PHI, bins=N)
	axs[1].set_ylabel('N')
	axs[1].set_xlabel('PHI');
	plt.show()
mode = "start"
while mode != "-1":
	match mode:
		case "start":
			file_name = input("ВВЕДИТЕ НАЗВАНИЕ ФАЙЛА: ") + '.txt'
			data_ = open(file_name, 'r')
			global data_r
			data_r = data_.read().splitlines()
			reading_pocess()
			'''
			for kskdnaklnfkdnamflkasnf in D:
				print(kskdnaklnfkdnamflkasnf)
			'''
		case "-1":
			print("nope")
			data_.close()
		case "0":
			#print("test")
			print("ДОСТУПНЫЕ РЕЖИМЫ РАБОТЫ:\n-1=ВЫКЛЮЧЕНИЕ\n 0=ПОМОЩЬ\n 1=ГРАФИК ИЗМЕНЕНИЯ ФУНКЦИИ\n 2=ОТРИСОВКА КОНЕЧНОГО СОСТОЯНИЯ\n 3=ПОВЕРКА РАСПРЕДЕЛЕНИЯ\nПРЕЖДЕ ЧЕМ ИЗМЕНИТЬ ВВОД, УБЕДИТЕСЬ, ЧТО ОКНО ВЫВОДА ЗАКРЫТО")
		case "1":
			graf_()
		case "2":
			sphere_drawer()
		case "3":
			distribution_check()
		case _:
			print("Error: invalid mode value")
	if mode !="start":
		mode = input("ВВЕДИТЕ РЕЖИМ ОБРАБОТКИ: ") # РЕЖИМ ВЫВОДА
	else:
		mode = "0"
