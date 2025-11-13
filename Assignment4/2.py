#Create a Pandas Series of 5 numbers and demonstrate insertion and deletion of an element.
import pandas as pd

# Create a Pandas Series of 5 numbers
series = pd.Series([10, 20, 30, 40, 50])

# Insert an element (e.g., 25 at index 2)
series = series.append(pd.Series([25], index=[2])).sort_index().reset_index(drop=True)

# Delete an element (e.g., element at index 3)
series = series.drop(3).reset_index(drop=True)

print(series)