import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('61bcb8fd-1630-46c2-857a-db3d51ac73e0.csv', sep = ';')
x = df[df['product'] == 'BANANAS']['timestamp']
y = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 100).mean()
std = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 100).std()
BOLU = y + 1.5 * std
BOLD = y - 1.5 * std

plt.plot(x, df[df['product'] == 'BANANAS']['mid_price'], color = 'r')
plt.plot(x, y)
plt.plot(x, BOLU)
plt.plot(x, BOLD)
plt.show()

print(BOLU[len(BOLU)-1])
print(BOLD[len(BOLD)-1])
