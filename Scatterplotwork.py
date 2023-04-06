import pandas as pd
from matplotlib import pyplot as plt

# print(plt.style.available)


# x = [1,4,5,2,3,6,2,3,4,6,3,3,4,2,6,2]
# y = [4,2,5,3,4,6,3,5,1,2,5,2,1,4,2,7]

# colors = [1,2,5,2,1,3,5,6,2,3,6,2,1,4,2,5]
# sizes = [13,121,53,21,215,54,21,25,41,12,51,25,52,12,25,34]
# print(len(colors))

# print(len(y))   We do this to make sure both lists have the same length

# plt.scatter(x,y, s=sizes, c =colors, marker = 'o', cmap = 'Greens', edgecolor = 'black', linewidth=1, alpha = 0.75)

# pass a color bar legend
# What do you want the dark and lighter shades to mean in your plot

# We now must work with a csv that we import

raw_data = pd.read_csv('data2.csv')
# print(raw_data.head(4))     Just to check to see we imported the correct information

views = raw_data['view_count']
likes = raw_data['likes']
ratio = raw_data['ratio']
# we can put the color to the scaling, and cmap with a color SCHEME / STYLE
# this results in better output

plt.scatter(views, likes, c = ratio, cmap='summer', edgecolor = 'black', linewidth=1, alpha = 0.75)


# Marking the xscale and yscale to logs make it so that the whole plot
# Can be seen no matter how far away the plots are

plt.xscale('log')
plt.yscale('log')


plt.title('Trending Youtube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

# Since colors are set to the ratio, we have the editing of the cbar and cmap here

cbar = plt.colorbar()

# We set the label of the range of the colors to what 
cbar.set_label('Like-Dislike Ratio')

plt.show()