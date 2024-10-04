import numpy as np

path = "unlabelled_data.csv"

data_list=[]
with open(path, "r") as data:
    for row in data:
        row_list=row.strip().split(",")
        data_list.append(row_list)
cn=0
cm=0

for k in np.linspace(-5, -0, 51):
    cn=0
    cm=0
    for j in data_list:
        x=float(j[0])
        y=float(j[1])
        if y>(k*x):
            j.append(1)
            cn=cn+1
        else:
            j.append(0)
            cm=cm+1

    print(round(k, 3), cn, cm)
