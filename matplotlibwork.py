from matplotlib import pyplot as plt
print(plt.style.available)
plt.style.use('fivethirtyeight')
import numpy as np

# dev_x  = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]     ##   This got replaced with ages

dev_y = [38496, 42000, 46752, 49320, 52300, 56000,
         69404,69642, 72104, 74020, 82011]
#  This infomation is about developers of either language
 # We now want to look at developers who specifically professionalize in python

# We see that the bars overlap on the bar chart so trying to justidy both plausible charts will be possible using numpy, so we import numpy as np

ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45314, 53124, 55636, 62453, 65534, 67743, 72431,
             81233, 86336, 95522, 103122]

js_dev_y = [47821, 48249, 52394, 59913, 62039, 68923, 72349, 78284, 82239, 84499, 96293]

x_indexes = np.arange(len(ages))
width = 0.25

# plt.plot(ages, dev_y, color='#413994', linestyle='dotted', linewidth=3, label='All Devs')
        # Plot the linear model of the two lists and values within those lists   ## Replace the color and linestyle with 'k--'

# plt.plot(ages, py_dev_y, color='#521334', linestyle='solid' ,linewidth=3, label='Python Devs')
        # Plotting python specific developers and their salaries

# Bar chart instead this time

plt.bar(x_indexes, dev_y, width = width, color="#881931", label="All Devs")

plt.bar(x_indexes-width,py_dev_y, width = width, color="#134231", label="Python Devs")

plt.bar(x_indexes+width, js_dev_y, width = width, color="#312311", label="JS Devs")

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')  #  Mark an x axis label
plt.ylabel('Median Salary (USD)')  # Mark a y axis label
# plt.legend(['All Devs', 'Python Devs'])
    # Replaced by the label argument in plt.plot

# You can use hexdata colors in the color string for a specific color  as #419348    (6 Numbers)
# Let us say we wanted to increase the size of the lines on the plot
    #  We can do this with linewidth in the arguments of the plt.plot

plt.legend()
plt.xticks(ticks=x_indexes, labels = ages)

# We can input some padding with the phrasing below
plt.tight_layout()
#  plt.grid(True)     # this input is to place a grid behind our marked lines to give us a better understanding of the graph

#  plt.savefig('plot.png')    # saves the plot as it's own png photo
plt.show()

