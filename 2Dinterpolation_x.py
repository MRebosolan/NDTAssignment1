import numpy as np
import seaborn as sns
import scipy.interpolate as ip
import matplotlib.pyplot as plt
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

n_rows = 8
n_columns = 50


x_coord = []
y_coord = []

pi00 = open("pi_00.txt")
for n, line in enumerate(pi00):
    line = line.strip(" ").split("	   ")
    line = [float(i) for i in line]
    for j, elem in enumerate(line[:-1]):
        y_coord.append(elem)
        break

pj00 = open("pj_00.txt")
for m, line1 in enumerate(pj00):
    line1 = line1.strip(" ").split("	   ")
    line1 = [float(i) for i in line1]
    for k, elem1 in enumerate(line1[:-1]):
        x_coord.append(elem1)
    break

x_coord = np.array(x_coord)
y_coord = np.array(y_coord)

test_strain_x = open("test_strain_x_all.txt")
lines = []
for line2 in test_strain_x:
    lines.append(line2)

#EXTRACT STRAIN DATA OF 1ST IMAGE -- STRAINXY WHERE X=IMAGE, Y=SET OF COLUMNS (1 THROUGH 13, 14 THROUGH 26 ETC.)

for n, line in enumerate(lines[4:12]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain11 = np.zeros((1, len(line)))
    strain11 = np.vstack((strain11, np.array(line)))

strain11 = np.delete(strain11, 0, 0)


for n, line in enumerate(lines[15:23]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain12 = np.zeros((1, len(line)))
    strain12 = np.vstack((strain12, np.array(line)))

strain12 = np.delete(strain12, 0, 0)


for n, line in enumerate(lines[26:34]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain13 = np.zeros((1, len(line)))
    strain13 = np.vstack((strain13, np.array(line)))

strain13 = np.delete(strain13, 0, 0)


strain1 = np.hstack((strain11, strain12, strain13))


#EXTRACT STRAIN DATA OF 2ND IMAGE


for n, line in enumerate(lines[40:48]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain21 = np.zeros((1, len(line)))
    strain21 = np.vstack((strain21, np.array(line)))

strain21 = np.delete(strain21, 0, 0)


for n, line in enumerate(lines[51:59]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain22 = np.zeros((1, len(line)))
    strain22 = np.vstack((strain22, np.array(line)))

strain22 = np.delete(strain22, 0, 0)


for n, line in enumerate(lines[62:70]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain23 = np.zeros((1, len(line)))
    strain23 = np.vstack((strain23, np.array(line)))

strain23 = np.delete(strain23, 0, 0)


for n, line in enumerate(lines[73:81]):
    line = line.strip(" ").strip("\n").split("   ")
    while "" in line:
        line.remove("")
    line = [x if x != " NaN" else 0 for x in line]
    line = [float(i) for i in line]
    if n == 0:
        strain24 = np.zeros((1, len(line)))
    strain24 = np.vstack((strain24, np.array(line)))

strain24 = np.delete(strain24, 0, 0)

strain2 = np.hstack((strain21, strain22, strain23, strain24))

#EXTRACT STRAIN DATA OF 3RD IMAGE


for n, line in enumerate(lines[87:95]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain31 = np.zeros((1, len(line)))
    strain31 = np.vstack((strain31, np.array(line)))

strain31 = np.delete(strain31, 0, 0)


for n, line in enumerate(lines[98:106]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain32 = np.zeros((1, len(line)))
    strain32 = np.vstack((strain32, np.array(line)))

strain32 = np.delete(strain32, 0, 0)


for n, line in enumerate(lines[109:117]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain33 = np.zeros((1, len(line)))
    strain33 = np.vstack((strain33, np.array(line)))

strain33 = np.delete(strain33, 0, 0)


for n, line in enumerate(lines[120:128]):
    line = line.strip(" ").strip("\n").split("   ")
    while "" in line:
        line.remove("")
    line = [x if x != " NaN" else 0 for x in line]
    line = [float(i) for i in line]
    if n == 0:
        strain34 = np.zeros((1, len(line)))
    strain34 = np.vstack((strain34, np.array(line)))

strain34 = np.delete(strain34, 0, 0)
strain3 = np.hstack((strain31, strain32, strain33, strain34))

#EXTRACT STRAIN DATA OF 4TH IMAGE


for n, line in enumerate(lines[134:142]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain41 = np.zeros((1, len(line)))
    strain41 = np.vstack((strain41, np.array(line)))

strain41 = np.delete(strain41, 0, 0)


for n, line in enumerate(lines[145:153]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain42 = np.zeros((1, len(line)))
    strain42 = np.vstack((strain42, np.array(line)))

strain42 = np.delete(strain42, 0, 0)


for n, line in enumerate(lines[156:164]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain43 = np.zeros((1, len(line)))
    strain43 = np.vstack((strain43, np.array(line)))

strain43 = np.delete(strain43, 0, 0)


for n, line in enumerate(lines[167:175]):
    line = line.strip(" ").strip("\n").split("   ")
    while "" in line:
        line.remove("")
    line = [x if x != " NaN" else 0 for x in line]
    line = [float(i) for i in line]
    if n == 0:
        strain44 = np.zeros((1, len(line)))
    strain44 = np.vstack((strain44, np.array(line)))

strain44 = np.delete(strain44, 0, 0)

strain4 = np.hstack((strain41, strain42, strain43, strain44))

#EXTRACT STRAIN DATA OF 5TH IMAGE


for n, line in enumerate(lines[181:189]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain51 = np.zeros((1, len(line)))
    strain51 = np.vstack((strain51, np.array(line)))

strain51 = np.delete(strain51, 0, 0)


for n, line in enumerate(lines[192:200]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain52 = np.zeros((1, len(line)))
    strain52 = np.vstack((strain52, np.array(line)))

strain52 = np.delete(strain52, 0, 0)


for n, line in enumerate(lines[203:211]):
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    if n == 0:
        strain53 = np.zeros((1, len(line)))
    strain53 = np.vstack((strain53, np.array(line)))

strain53 = np.delete(strain53, 0, 0)


for n, line in enumerate(lines[214:222]):
    line = line.strip(" ").strip("\n").split("   ")
    while "" in line:
        line.remove("")
    line = [x if x != " NaN" else 0 for x in line]
    line = [float(i) for i in line]
    if n == 0:
        strain54 = np.zeros((1, len(line)))
    strain54 = np.vstack((strain54, np.array(line)))

strain54 = np.delete(strain54, 0, 0)

strain5 = np.hstack((strain51, strain52, strain53, strain54))

e = ip.interp2d(x_coord, y_coord, strain1, kind="cubic")
x2 = np.arange(x_coord[0], x_coord[-1], 1)
y2 = np.arange(y_coord[0], y_coord[-1], 1)
strain1func = e(x2, y2)

f = ip.interp2d(x_coord, y_coord, strain2, kind="cubic")
x2 = np.arange(x_coord[0], x_coord[-1], 1)
y2 = np.arange(y_coord[0], y_coord[-1], 1)
strain2func = f(x2, y2)

g = ip.interp2d(x_coord, y_coord, strain3, kind="cubic")
x2 = np.arange(x_coord[0], x_coord[-1], 1)
y2 = np.arange(y_coord[0], y_coord[-1], 1)
strain3func = g(x2, y2)

h = ip.interp2d(x_coord, y_coord, strain4, kind="cubic")
x2 = np.arange(x_coord[0], x_coord[-1], 1)
y2 = np.arange(y_coord[0], y_coord[-1], 1)
strain4func = h(x2, y2)

i = ip.interp2d(x_coord, y_coord, strain5, kind="cubic")
x2 = np.arange(x_coord[0], x_coord[-1], 1)
y2 = np.arange(y_coord[0], y_coord[-1], 1)
strain5func = i(x2, y2)

strain_functions = [strain1func, strain2func, strain3func, strain4func, strain5func]


for n, function in enumerate(strain_functions):
    im = imshow(function, cmap=cm.YlGnBu)  # drawing the function
    colorbar(im) # adding the colorbar on the right
    title(f'image {n+1} x strain')
    show()


