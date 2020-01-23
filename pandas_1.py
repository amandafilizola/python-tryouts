#!/usr/bin/env python
import pandas as pd

data = [['thomas', 10], ['alannon', 15], ['juli', 14]]

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)


# initialise data of lists.
data = {
    'Name':
    ['Tom', 'Jack', 'nick', 'juli'],
    'marks':
    [99, 98, 95, 90]
}

# Creates pandas DataFrame.
df2 = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])

# print the data
print(df2)

# Initialise data to lists.
data3 = [{'a': 1, 'b': 2, 'c':3}, {'a':10, 'b': 20, 'c': 30}]

# Creates DataFrame.
df3 = pd.DataFrame(data3)

# Print the data
print(df3)


