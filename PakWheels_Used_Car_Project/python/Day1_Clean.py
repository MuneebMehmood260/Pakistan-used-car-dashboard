import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"PakWheels_Used_Car_Dataset.xlsx")
# print(df.head(5))
# print(df.shape)
# print(df["Ad_ID"].dtypes)

# ===================================================================
#                        Duplicate Detect and Removal
# ===================================================================
# print("Total Rows : ", len(df))
# print("Unique Rows of Ad_ID : ", df["Ad_ID"].nunique())
# print("Duplicate Rows of Ad_ID : ", df["Ad_ID"].duplicated().sum())
# #only 1 value null ha 

compare_cols = [c for c in df.columns if c != 'Ad_ID']

# (original + copy )
# print(df.duplicated(subset=compare_cols, keep=False).sum())

# #kitni "extra" copies hain jo remove karni hain
# print(df.duplicated(subset=compare_cols, keep='first').sum())

## Show Duplicate values
 
# dup = df[df.duplicated(subset=compare_cols, keep=False)]
# print(dup.sort_values(by=compare_cols).head(10))

df = df.drop_duplicates(subset=compare_cols, keep='first').reset_index(drop=True)
# print("Rows after removing duplicates:", len(df))
# print(df.duplicated().sum())
# ===================================================================
#                        Inconsistence Values Detection 
# ===================================================================

cat_cols = ['Brand', 'Fuel_Type', 'Transmission', 'City']


for col in cat_cols:
    df[col] = df[col].str.strip()          # extra spaces hatao (aage/peeche)
    
df["City"] = df["City"].replace({
    'FAISALABAD' : 'Faisalabad',
    'faisalabad' : 'Faisalabad',
    'ISLAMABAD' : 'Islamabad',
    'Isb' : 'Islamabad',
    'islamabad' : 'Islamabad',
    'islamabad' : 'Islamabad',
    'KARACHI' : 'Karachi',
    'Khi' : 'Karachi',
    'karachi' : 'Karachi',
    'LAHORE' : 'Lahore',
    'lahore' : 'Lahore',
    'Lhr' : 'Lahore',
    'Pindi' : 'Rawalpindi',
    'RAWALPINDI' : 'Rawalpindi',
    'rawalpindi' : 'Rawalpindi',
}) 
df["Brand"] = df["Brand"].replace({
    'HONDA' : 'Honda',
    'honda' : 'Honda',
    'honda' : 'Honda',
    'KIA' : 'KIA',
    'kia' : 'KIA',
    'SUZUKI' : 'Suzuki',
    'suzuki' : 'Suzuki',   
    'TOYOTA' : 'Toyota',   
    'toyota' : 'Toyota',
})
df["Fuel_Type"] = df["Fuel_Type"].replace({
    'Cng' : 'CNG',
    'cng' : 'CNG',
    'DIESEL' : 'Diesel',
    'diesel' : 'Diesel',
    'PETROL' : 'Petrol',
    'petrol' : 'Petrol',
    'HYBRID' : 'Hybrid',
    'hybrid' : 'Hybrid'
})
df["Transmission"] = df["Transmission"].replace({
    'MANUAL' : 'Manual',
    'Man' : 'Manual',
    'Man.' : 'Manual',
    'manual' : 'Manual',
    'AUTOMATIC' : 'Automatic',
    'Auto' : 'Automatic',
    'Auto.' : 'Automatic',
    'automatic' : 'Automatic'
})

# for col in cat_cols:
#     print(col, "->", sorted(df[col].dropna().unique()))
#     print(col, "->", df[col].nunique())
# ===================================================================
#                        Missing Values Detection
# ===================================================================

for col in ['Fuel_Type', 'Transmission', 'City']:
    df[col] = df[col].fillna(df[col].mode()[0])  # fill missing values with mode

df["Color"] = df["Color"].fillna("Unknown")  # fill missing values with Unknown

for col in ['Engine_Capacity_cc', 'Mileage_km', 'Price_PKR']:
    df[col] = df[col].fillna(df[col].median())  # fill missing values with median

df['Number_of_Owners'] = df['Number_of_Owners'].fillna(df['Number_of_Owners'].mode()[0])

# print(df.isnull().sum())
# print("===================================================================")
# print((df.isnull().sum() / len(df) * 100).round(2))

# ====================================================================

valid_year_mask = (df['Manufacturing_Year'] >= 1990) & (df['Manufacturing_Year'] <= 2026)
# print("Invalid year rows:", (~valid_year_mask).sum())

df = df[valid_year_mask].reset_index(drop=True)

Q1 = df['Price_PKR'].quantile(0.25)
Q3 = df['Price_PKR'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# print("Lower bound:", lower_bound)
# print("Upper bound:", upper_bound)

df['Price_PKR'] = df['Price_PKR'].clip(lower=lower_bound, upper=upper_bound)

Q1 = df['Mileage_km'].quantile(0.25)
Q3 = df['Mileage_km'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Mileage_km'] = df['Mileage_km'].clip(lower=max(0, lower_bound), upper=upper_bound)

# print(df['Price_PKR'].describe())
# print(df['Mileage_km'].describe())
# print("Final rows:", len(df))

df["Mileage_km"] = df["Mileage_km"].astype(int)
df['Manufacturing_Year'] = df['Manufacturing_Year'].astype(int)
df['Price_PKR'] = df['Price_PKR'].astype(int)
# Koi bhi car Rs. 50,000 se kam ki nahi ho sakti - ye business logic hai
df.loc[df['Price_PKR'] < 50000, 'Price_PKR'] = df['Price_PKR'].median()
# print(df.info())

# df.to_excel(r"PakWheels_Used_Car_Dataset.xlsx", index=False)