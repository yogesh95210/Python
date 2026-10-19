from pathlib import Path
import pandas as pd

# Automatically finds the directory where this script resides
script_dir = Path(__file__).parent
csv_path = script_dir / "data.csv"

# Load and print data
df = pd.read_csv(csv_path)
print(df.to_string())



