# КОМПИЛЯЦИЯ ГРАФИКОВ ПРИ N=6, MCS=1000000 И РАЗЛИЧНЫХ jump_max
import matplotlib.pyplot as plt
fl_1 = open("project_data_4_r1_N6_MCS1000000_j1_experiment.txt", 'r')
fl_1_r = fl_1.read().splitlines()
fl_2 = open("project_data_4_r1_N6_MCS1000000_j3.txt", 'r')
fl_2_r = fl_2.read().splitlines()
fl_3 = open("project_data_4_r1_N6_MCS1000000_j6.txt", 'r')
fl_3_r = fl_3.read().splitlines()
fl_4 = open("project_data_4_r1_N6_MCS1000000_j12.txt", 'r')
fl_4_r = fl_4.read().splitlines()

a, b, c, d = [], [], [], []
for i in range(len(fl_1_r)):
	a_i = fl_1_r[i].split()
	a.append([float(a_i[1]), float(a_i[2])])

for i in range(len(fl_2_r)):
	b_i = fl_2_r[i].split()
	b.append([float(b_i[1]), float(b_i[2])])

for i in range(len(fl_3_r)):
	c_i = fl_3_r[i].split()
	c.append([float(c_i[1]), float(c_i[2])])

for i in range(len(fl_4_r)):
	d_i = fl_4_r[i].split()
	d.append([float(d_i[1]), float(d_i[2])])

'''
a = [[i, i+2] for i in range(10)]
b = [[i, 2*i] for i in range(8)]
'''
a_x = []
a_y = []
for i in range(len(a)):
	a_x.append(a[i][0])
	a_y.append(a[i][1])

b_x = []
b_y = []
for i in range(len(b)):
	b_x.append(b[i][0])
	b_y.append(b[i][1])

c_x = []
c_y = []
for i in range(len(c)):
	c_x.append(c[i][0])
	c_y.append(c[i][1])

d_x = []
d_y = []
for i in range(len(d)):
	d_x.append(d[i][0])
	d_y.append(d[i][1])

plt.plot(a_x, a_y, color='r')
plt.plot(b_x, b_y, color='g')
plt.plot(c_x, c_y, color='b')
plt.plot(d_x, d_y, color='black')
#plt.scatter(a_x, a_y, s=2, color="r")
#plt.xlabel('MCS') 
#plt.ylabel('F')
plt.show()

