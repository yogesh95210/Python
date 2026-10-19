import pandas as pd

# Load the JSON file using forward slashes
df = pd.read_json('C:/Python/Basics/Pandas/data.json')
print(df.to_string())
