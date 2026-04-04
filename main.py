# call in libraries

import pandas as pd 
import numpy as np

# import data
df = pd.read_csv("C:/Users/HP/Downloads/archive/dirty_cafe_sales.csv")
print("Raw Data good to go!")


# Check for duplicates

df = df.drop_duplicates()
print("No duplicates.")


# modifying and standardizing column.

df = df.replace({
    "Total Spent": {"ERROR": np.nan}, 
    "Payment Method":{"UNKNOWN": "Unknown"},
    "Location":{"UNKNOWN": "Unknown"}})

print("Modified!")


# convert total spent, price per unit to 'float' instead of str (initial data type)

for col in ["Price Per Unit","Total Spent"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


print("Fixed!")


#confirm data type conversion.

df = df[["Price Per Unit","Total Spent"]].dtypes

print("Confirmed!")


# print("Filled!")
# print(type(df))
print(df)
if hasattr(df, 'columns'):
    print(df.columns.tolist())



# convert float to rounded figure

for col in ["Price Per Unit","Total Spent"]:
    df[col] = df[col].round(1)

print("Fixed")



# replacing null values in the Item column with 'Not Listed' 

df["Item"] = df["Item"].replace(np.nan, "Not Listed")

print("Done!")





# replace nan values with 'Unknown' in specified columns. 

df = df.replace(np.nan,"Unknown")

print("Values replaced!")


# Export cleaned data to Excel xlsx file.

df.to_excel("cleaned_cafe_sales_data.xlsx", index=False, engine="openpyxl")
print("Done!")


# import openpyxl for data validation rules.

from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation

wb = load_workbook("cleaned_cafe_sales_data.xlsx")
ws = wb.active

print("Active!")



# Setting data validation rules for column D must be equal or greater than zero 0. 


dv = DataValidation(type="whole",operator="greaterThanOrEqual",formula1="0")
ws.add_data_validation(dv)
dv.add("D2:D10000")

print("Enforced_Law 1!")


# Setting data validation rules for column E must be equal or greater than zero 0. 


dv = DataValidation(type="whole",operator="greaterThanOrEqual",formula1="0")
ws.add_data_validation(dv)
dv.add("E2:E10000")

print("Enforced_Law 2!")


# Setting data validation rules for column H must not be future date. 

dv = DataValidation(type="date",operator="greaterThanOrEqual",formula1="TODAY()", allow_blank=False)
ws.add_data_validation(dv)
dv.add("H2:H10000")

print("Enforced_Law3!")



# File saved in xlsx format to be exported to Excel for data processing.

wb.save("cleaned_cafe_sales_data.xlsx")
print("File saved in xlsx format!")



# Save file to csv format in local directory.

df.to_csv("C:/Users/HP/Downloads/cleaned_cafe_sales_data.csv",index=False)
print("Ready!")
