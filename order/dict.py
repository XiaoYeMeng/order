import pandas as pd
custom = pd.read_excel('custom.xlsx', sheet_name='sheet_1', usecols='A, B')

print(custom)
