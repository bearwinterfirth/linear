import numpy as np
import matplotlib.pyplot as plt

path1 = "unlabelled_data.csv"
path2 = "labelled_data.csv"

k = -1.5                # k=slope
m = 0.2                 # m=intersect

data_list=[]            # all points will be stored here
x0, y0, x1, y1 = [], [], [], []     # separate lists for easier plotting

def read_unlabelled_data():
    with open(path1, "r") as data:
        for row in data:
            row_list=row.strip().split(",")
            data_list.append(row_list)
    
    for j in data_list:     # each datapoint is appended with 0 (below line) or 1 (above line)
        x=float(j[0])
        y=float(j[1])
        if y>(k * x + m):
            j.append(1)  
        else:
            j.append(0)

def plot_line():
    x_values=np.linspace(-5,5,11)
    y_values=[k * x + m for x in x_values]
    plt.plot(x_values, y_values)

def make_lists_by_classes():
    class_0 = [row for row in data_list if row[2]==0]
    class_1 = [row for row in data_list if row[2]==1]    
    for j in class_0:
        x0.append(float(j[0]))
        y0.append(float(j[1]))
    for j in class_1:
        x1.append(float(j[0]))
        y1.append(float(j[1]))

def plot_points():
    plt.scatter(x0, y0, color="b")
    plt.scatter(x1, y1, color="r")
    plt.legend([f"y={k}x+{m}", "Class 0", "Class 1"], loc="upper left")
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.grid()
    plt.show()

def write_labelled_data():
    with open(path2, "w", newline='') as labelled:
        for row in data_list:
            labelled.write(f"{row[0]}, {row[1]}, {row[2]}\n")
                       
read_unlabelled_data()
plot_line()
make_lists_by_classes()
plot_points()
write_labelled_data()


