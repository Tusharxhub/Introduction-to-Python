#Create a Pandas Series of 5 numbers and demonstrate insertion and deletion of an element.(Hint: Use pd.Series(), .drop(), and pd.concat()).Create a Pandas Series of 5 numbers and demonstrate insertion and deletion of an element.


import pandas as pd

series = pd.Series([10, 20, 30, 40, 50])
series = pd.concat(
    [series.iloc[:2], pd.Series([25], index=[2]), series.iloc[2:]]
).reset_index(drop=True)

series = series.drop(3).reset_index(drop=True)

print(series)