from matplotlib import pyplot as plt
%matplotlib inline

#style method
plt.style.use('fivethirtyeight')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748]

plt.plot(ages_x, dev_y, color='#444444', linestyle='--' ,label='All Devs')

#plot salary for python developer
py_dev_y = [20046, 17100, 20000, 24744, 30500,
            37732, 41247, 45372, 48876, 53850]

plt.plot(ages_x, py_dev_y, color='#008fd5',linewidth=3 ,label='Python')

#plot salary for js developer
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746]

plt.plot(ages_x, js_dev_y, color='#e5ae38' ,label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()

plt.tight_layout()

#save image file
plt.savefig('plot1.png')

plt.show()