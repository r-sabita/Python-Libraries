from matplotlib import pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
import csv
from collections import Counter

#style method
plt.style.use('fivethirtyeight')

#with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
 
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
   
language_counter = Counter()
    
for response in lang_responses:
    language_counter.update(response.split(';'))
   
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
    
languages.reverse()
popularity.reverse()

#plot horizontal bar chart 'barh'
plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Number of People Who Use')

plt.tight_layout()

plt.savefig('csv_barplot.png')

 