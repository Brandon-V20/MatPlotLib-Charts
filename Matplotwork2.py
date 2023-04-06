import csv
from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
plt.style.use('seaborn-v0_8')

# with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
data = pd.read_csv("data.csv")
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

print(languages)
print(popularity)

plt.barh(languages, popularity, color='#492004')  # plt.bar just shows a vertical bar chart. Barh makes it as a horizontal bar chart

plt.title("Most Popular Dev Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number of Developers")
plt.tight_layout()
plt.grid(False)
plt.show()


#    row = next(csv_reader)
#    print(row['LanguagesWorkedWith'].split(';'))

# data = pd.read_csv('data.csv')
# print(data.head(10))

