import numpy as np
import seaborn as sns

n_rows = 8
n_columns = 50


x_coord = []
y_coord = []

pi00 = open("pi_00.txt")
for n, line in enumerate(pi00):
    line = line.strip(" ").split("	   ")
    line = [float(i) for i in line]
    for j, elem in enumerate(line):
        x_coord.append(elem)


pj00 = open("pj_00.txt")
for m, line1 in enumerate(pj00):
    line1 = line1.strip(" ").split("	   ")
    line1 = [float(i) for i in line1]
    for k, elem1 in enumerate(line1):
        y_coord.append(elem1)


test_strain_x = open("test_strain_x_all.txt")
lines = []
for line2 in test_strain_x:
    lines.append(line2)

#EXTRACT STRAIN DATA OF 1ST IMAGE
strain1 = []

for line in lines[40:49]:
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    strain1.append(line)


for line in lines[51:59]:
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    strain1.append(line)

for line in lines[62:70]:
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    strain1.append(line)

for line in lines[73:81]:
    line = line.strip(" ").strip("\n").split("   ")
    line = [x if x != "NaN" and x != "nan" else 0 for x in line]
    while "" in line:
        line.remove("")
    line = [float(i) for i in line]
    strain1.append(line)

print(strain1)
ax = sns.heatmap(strain1[0:8], cmap="YlGnBu")