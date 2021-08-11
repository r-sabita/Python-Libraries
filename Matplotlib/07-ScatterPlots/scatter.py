import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

#x = [1,2,3,5,2,5,6,7,3,9,8,4] 
#y = [2,5,6,7,1,2,3,5,3,9,8,4] 
#colors = [8,5,6,7,4,2,9,5,3,9,8,4] 
#sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 399]
#plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.75)
#cbar = plt.colorbar()
#cbar.set_label('Satisfaction')

data = pd.read_csv('data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio edgecolor='black',
            linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()