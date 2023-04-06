from matplotlib import pyplot as plt
# print(plt.style.available)

plt.style.use('_classic_test_patch')

slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#']
explode = [.3, 0, 0, 0, 0, 0, 0]

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'},
        rotatelabels=10, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%')
# We can bring out a piece of the pie with the explode method
# We may also be able to twist the whole chart with startangle = whatever degrees
# The shadow portion behind each piece can be justified with the shadow = True statement


plt.title("My first Pie Chart")
plt.tight_layout()
plt.show()

