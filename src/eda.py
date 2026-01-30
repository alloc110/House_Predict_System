import os
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

folder_path = 'data'
file_name = 'AAPL_data.csv'
full_path = os.path.join(folder_path, file_name)

# BƯỚC QUAN TRỌNG: Nếu thư mục chưa có, thì tạo nó
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Đã tạo thư mục: {folder_path}")


# Download 1 year of daily data for Apple
data = yf.download("AAPL", period="max", interval="1d")
data.to_csv(full_path)

### EDA
# Print the columns
print(data.columns)
print("Print the first few rows")
print(data.head())
print("Done printing the first few rows")
print()

print("Check info few rows")
print(data.info())
print("Done printing info few rows")
print()

print("Check for missing values")
print(data.isnull().sum())
print("Done check for missing values")
print()

print("Describe data")
print(data.describe())
print("Done describe data")
print()


# Data Visualization
data['Close'].plot(figsize=(10, 6), color='blue', title='Giá cổ phiếu Apple')

# Thêm lưới và nhãn
plt.grid(True)
plt.ylabel('Giá (USD)')
plt.xlabel('Ngày')
plt.show()


data['Return'] = data['Close'].pct_change()
plt.figure(figsize=(10, 6))
sns.histplot(data['Return'].dropna(), bins=100, kde=True, color='purple')
plt.title('Phân phối lợi nhuận hàng ngày (Daily Returns)')
plt.show()
