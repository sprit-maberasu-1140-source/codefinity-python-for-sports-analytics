import pandas as pd

# Create the DataFrame and assign it to 'df'
data = {
    "Date": ["2024-04-01", "2024-04-02", "2024-04-03", "2024-04-04", "2024-04-05"],
    "Home Team": ["Lions", "Tigers", "Bears", "Wolves", "Eagles"],
    "Away Team": ["Eagles", "Wolves", "Tigers", "Lions", "Bears"],
    "Home Score": [3, 2, 1, 0, 4],
    "Away Score": [1, 2, 2, 3, 2]
}

df = pd.DataFrame(data)
for row in df.head().values:
    print(*row)
df.info()