import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt
from matplotlib import dates as mpl_dates
from datetime import timedelta as tda

# dates = [
#    dt(2019, 5, 24),
#    dt(2019, 5, 25),
#    dt(2019, 5, 26),
#    dt(2019, 5, 27),
#    dt(2019, 5, 28),
#    dt(2019, 5, 29),
#    dt(2019, 5, 30)
#    ]

# y = [0,1,3,4,6,5,7]

# Plot and after we work with axis
# place linestyle to solid to set the connector to the points to be a line
plt.style.use('fast')
data = pd.read_csv('bitcoin_data.csv')

data['Date'] = pd.to_datetime(data['Date'])

# We must sort the values so that they are in order
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']
# we must check to see if the data is updated
print(price_date)

plt.plot_date(price_date, price_close, linestyle='solid')

# Get current format () is making the labels on the plot visible
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

