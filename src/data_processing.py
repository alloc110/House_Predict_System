import pandas as pd     
full_path = "data/AAPL_data.csv"

df = pd.read_csv(full_path)

print(df)
# Loại bỏ hai hàng đầu tiên không cần thiết
df = df.drop([0,1])
df.reset_index(drop=True, inplace=True)
print(df)