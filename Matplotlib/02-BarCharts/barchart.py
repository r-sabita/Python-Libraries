from matplotlib import pyplot as plt
%matplotlib inline
import numpy as np

#style method
plt.style.use('fivethirtyeight')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

x_indexes = np.arange(len(ages_x))

#create width variable for plotting all three inpus side by side
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748]

plt.bar(x_indexes - width, dev_y, color='#444444', width=width, linestyle='--' ,label='All Devs')

#plot salary for python developer
py_dev_y = [20046, 17100, 20000, 24744, 30500,
            37732, 41247, 45372, 48876, 53850]

plt.bar(x_indexes, py_dev_y, color='#008fd5', width=width, linewidth=3 ,label='Python')

#plot salary for js developer
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746]

plt.bar(x_indexes + width, js_dev_y, color='#e5ae38', width=width, label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()

#xticks() method to change the x labels
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.tight_layout()

#save image file
plt.savefig('barplot.png')

plt.show()