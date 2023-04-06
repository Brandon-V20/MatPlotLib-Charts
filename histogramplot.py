from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn-v0_8')

# ages = [18,19,21,25,26,26,30,32,38,45,55]
#  import that data from the csv file data1
# we configure the ids and ages with the columns in the data set (data1)


data = pd.read_csv('data1.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10,20,30,40,50,60,70,80,90]

# bins are criteria and sections of the histogram plot that hold the bars of occurances


plt.hist(ages, bins = bins, edgecolor = 'black', log=True)

# We can bring in a median or a mean line
median = 29
color = '#871634'
width = 4

# This implements a vertical line that is visible
plt.axvline(median, color=color, label='Median Age', linewidth=width)

plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Occurances')
plt.tight_layout()

plt.show()
