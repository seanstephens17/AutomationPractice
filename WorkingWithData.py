import pandas as pd

pd.read_excel('Document Name')

df_geo = pd.read_excel('Document Name', index_col=0)
df_geo.head(2)

df_sales = pd.read_excel('Document Name / Directory', sheet_name='Sheet Name', index_col=1)
df_sales

df_sales2 = pd.read_excel('', sheet_name='', index_col=None, names=['A', 'B', 'C', 'D'])
df_sales2

# save to excel
df_sales.to_excel('filename')

# save to specific sheet
df_sales.to_excel('filename', sheet_name='', index=False)

# save to csv
df_sales.to_csv("Filename", index=False)
