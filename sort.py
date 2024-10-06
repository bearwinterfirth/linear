import numpy as np
import csv
import matplotlib.pyplot as plt
import statistics as st

path1 = "unlabelled_data.csv"
path2 = "labelled_data.csv"

k = -1.5               # k=slope
m = 0.2                 # m=intersect

x_values=np.linspace(-5,5,11)
y_values=[k * x + m for x in x_values]

data_list=[]
with open(path1, "r") as data:
    for row in data:
        row_list=row.strip().split(",")
        data_list.append(row_list)
    
    for j in data_list:
        x=float(j[0])
        y=float(j[1])
        if y>(k * x + m):
            j.append(1)  
        else:
            j.append(0)
        
class_0 = [row for row in data_list if row[2]==0]
class_1 = [row for row in data_list if row[2]==1]
print(len(class_0), len(class_1))

x0, x1, y0, y1 = [], [], [], []

for j in class_0:
    x0.append(float(j[0]))
    y0.append(float(j[1]))

for j in class_1:
    x1.append(float(j[0]))
    y1.append(float(j[1]))


# fig, ax = plt.subplots()
# ax.scatter(x, y, c=label)
# ax.legend(["Hej", "Hej2"])

plt.scatter(x0, y0, color="b")
plt.scatter(x1, y1, color="r")
plt.plot(x_values, y_values)
plt.legend(["Class 0", "Class 1", f"y={k}x+{m}"], loc="upper left")

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid()

plt.show()





with open(path2, "w", newline='') as labelled:
    for row in data_list:
        labelled.write(f"{row[0]}, {row[1]}, {row[2]}\n")
                       

