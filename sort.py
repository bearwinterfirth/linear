import numpy as np
import csv
import matplotlib.pyplot as plt

path1 = "unlabelled_data.csv"
path2 = "labelled_data.csv"

k = -2               # k=slope
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

x=[]
y=[]
label=[]

for k in data_list:
    x.append(float(k[0]))
    y.append(float(k[1]))
    label.append(float(k[2]))

plt.scatter(x, y, c=label)
plt.plot(x_values, y_values)
plt.xlim(-5,5)
plt.ylim(-5,5)

plt.show()



with open(path2, "w", newline='') as labelled:          # https://discuss.python.org/t/writing-to-csv-files-unwanted-blank-row-in-file/28391
    write=csv.writer(labelled)
    write.writerows(data_list)                          # https://www.geeksforgeeks.org/writing-csv-files-in-python/

# colors=["r", "g"]
#     plt.scatter()
#     plt.show()

