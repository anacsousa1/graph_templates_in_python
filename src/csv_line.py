import pandas as pd
import matplotlib.pyplot as plt

# Load data from a csv file
df = pd.read_csv('data/data.csv', header = 4)
headers = list(df.columns)

# Plot all columns in a line figure
# df.plot() # plot all columns
df.plot(x = headers[0], y = [headers[1],headers[2],headers[3]]) # plot specific columns

plt.show()