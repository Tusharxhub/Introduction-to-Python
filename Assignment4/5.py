#Write a Pandas program to handle missing data in a DataFrame by replacing all NaN values with the column's mean value.


import pandas as pd

data = {
    "A": [10, 12, None, 15],
    "B": [3.5, None, 4.2, 4.8],
    "C": [None, 7.1, 6.8, None],
}

df = pd.DataFrame(data)
df = df.fillna(df.mean(numeric_only=True))

print(df)