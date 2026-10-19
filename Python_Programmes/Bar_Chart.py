import matplotlib.pyplot as plt

x_axis = ["Burger","Pizza","Momos","Pasta","Roti"]
y_axis = [37, 40, 55, 35, 20]

plt.title("Food Consumption")
plt.bar(x_axis, y_axis, color = ["red","green","blue","cyan","orange"])
plt.show()