from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917, 31991]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'php']
explode = [0, 0, 0, 0.2, 0, 0]


plt.pie(slices, labels=labels, explode=explode, shadow=True,
         startangle=90, autopct='%1.1f%%',
         wedgeprops={'edgecolor': 'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.savefig('piechart.png')
plt.show()