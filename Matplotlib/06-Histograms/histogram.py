import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#plot histogram
plt.hist(ages, bins=bins, edgecolor='black', log=True, linewidth=2)

median_age = 29
color = "#fc4f30"

plt.axvline(median_age, color=color, label='Age Median')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('histplot.png')
plt.show()


