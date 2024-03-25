import pandas as pd

# Load the Excel file
file_path = '/mnt/data/FID_ResultsKNNmiyawaki.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()
