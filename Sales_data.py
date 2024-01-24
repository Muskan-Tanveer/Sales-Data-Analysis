import pandas as pd
import os 

data = {
    "Date":[20-2-2002,21-2-2002,22-2-2002,23-2-2002,24-2-2002,25-2-2002,26-2-2002,27-2-2002,28-2-2002,29-2-2002,30-2-2002],
    "Product":['pearls','palmolive','Maclay','Sunsilk','Colgate','Bioaqua','Head & Shoulers','Ponds','Fair & Lovely','Lifebouy','Pert plus'],
    "Quantity":[23,45,56,34,23,45,76,87,67,98,86],
    "price":[2000,234,567,453,3223,2323,1234,543,456,245,244],
    "Customer":['John Smith','Calera Hai','Sultan Kareem','Tanveer Mehmmood','Maheen Abbasi','Sumairah Nadeem','Kashif Khan','Salman Kareem','Ashi','Muskan Abbasi','Fizza Raza'],
    'City':['Karachi','Islamabad','Kashmir','Multan','Faisalabad','Rawalpindi','Hyderabd','Sukkar','Peshawar','Quetta','Sargodha']
}

#DATA EXPLORATION

#creating DataFrame
df = pd.DataFrame(data)

#converting to csv
df.to_csv('Sales_data.csv',index=False)

print(df)

#reading data from csv
df = pd.read_csv("Sales_data.csv")

print(df.head())

print("Missing Values:")
print(df.isnull().sum())
print("Summary:")
print(df.describe())

#DATA CLEANING
df = df.dropna()  #handle missing values
df = df.drop_duplicates()   #removing duplicates row

#ANALYSIS

#total sales for each product
total_sales_for_each_product = df.groupby('Product')['Quantity'].sum()

#identifying the most sold product
most_sold_product = total_sales_for_each_product.idxmax()

print(f'The most sold product is {most_sold_product}')
print(f"total sales for each product{total_sales_for_each_product}")

#Sales Data Analysis
