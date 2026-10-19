import matplotlib.pyplot as plt
values= [40,50,90,40,10]
names = ["Burger","Pizza","Momos","Pasta","Roti"]
plt.pie(values,labels=names)
plt.title("Food Consumption")
plt.show()
