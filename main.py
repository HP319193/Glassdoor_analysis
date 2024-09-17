import pandas as pd

file_path = 'glassdoor_output.csv'
data = pd.read_csv(file_path)

for index, row in data.iterrows():
    print(f"Index: {index}, Column1: {row['ISIN']}, Column2: {row['pros']}")