import pandas as pd , matplotlib.pyplot as plt , seaborn as sns

# ==========================================================================
#                         DAY 2 (EDA)
# ==========================================================================
df = pd.read_excel(r"PakWheels_Used_Car_Dataset.xlsx")

df['Manufacturing_Year'] = df['Manufacturing_Year'].astype(int)
df['Price_PKR'] = df['Price_PKR'].astype(int)
# Koi bhi car Rs. 50,000 se kam ki nahi ho sakti - ye business logic hai
df.loc[df['Price_PKR'] < 50000, 'Price_PKR'] = df['Price_PKR'].median()
# ==========================================================================
def Brand():
    print("========================================================================")
    print("Brand Analysis")
    print("========================================================================")
    print(df['Brand'].value_counts())
    print(df['Brand'].value_counts(normalize=True) * 100)   # percentage share
    print(df["Model"].value_counts().head(10))

    plt.figure(figsize=(10,6))
    sns.countplot(data=df, y='Brand', order=df['Brand'].value_counts().index,hue='Brand', palette='viridis',legend=False)

    for i in range(len(df['Brand'].value_counts())):
        plt.text(df['Brand'].value_counts().iloc[i], i, df['Brand'].value_counts().iloc[i], ha='left', va='center')

    plt.title('Number of Listings by Brand')
    plt.xlabel('Count')
    plt.ylabel('Brand')
    plt.tight_layout()
    plt.show()
Brand()

    
def manufacturing_year():
    print("========================================================================")
    print("manufacturing_year")
    print("========================================================================")
    print(df['Manufacturing_Year'].describe())
    plt.figure(figsize=(10,6))
    sns.histplot(df['Manufacturing_Year'], bins=10, kde=False, color='steelblue')
    
    plt.title('Distribution of Manufacturing Year')
    plt.xlabel('Manufacturing Year')
    plt.ylabel('Number of Listings')
    plt.tight_layout()
    plt.show()
manufacturing_year()

def fuel():
    print("========================================================================")
    print("Fuel Type Analysis")
    print("========================================================================")
    print(df['Fuel_Type'].value_counts())
    print(df['Fuel_Type'].value_counts(normalize=True) * 100)
    plt.figure(figsize=(7,7))
    df['Fuel_Type'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('deep'))
    plt.title('Fuel Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
fuel()

def transmission():
    print("========================================================================")
    print("Transmission Type Analysis")
    print("========================================================================")
    print(df['Transmission'].value_counts())
    print(df['Transmission'].value_counts(normalize=True) * 100)
    plt.figure(figsize=(6,5))
    sns.countplot(data=df, x='Transmission', palette='pastel')
    for i in range(len(df['Transmission'].value_counts())):
        plt.text(i, df['Transmission'].value_counts().iloc[i], df['Transmission'].value_counts().iloc[i], ha='center', va='bottom')
    plt.title('Transmission Type Distribution')
    plt.xlabel('Transmission')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
transmission()

def engine_capacity():
    print("========================================================================")
    print("Engine Capacity Analysis")
    print("========================================================================")
    print(df['Engine_Capacity_cc'].describe())
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df['Engine_Capacity_cc'], color='lightgreen')
    plt.title('Engine Capacity Distribution (Box Plot)')
    plt.xlabel('Engine Capacity (cc)')
    plt.tight_layout()
    plt.show()
engine_capacity()

def mileage():
    print("========================================================================")
    print("Mileage Analysis")
    print("========================================================================")
    print(df['Mileage_km'].describe())
    plt.figure(figsize=(10,6))
    sns.histplot(df['Mileage_km'], bins=30, color='coral')
    plt.title('Mileage Distribution')
    plt.xlabel('Mileage (km)')
    plt.ylabel('Number of Listings')
    plt.tight_layout()
    plt.show()
mileage()

def price():
    print("========================================================================")
    print("Price Analysis")
    print("========================================================================")
    print(df['Price_PKR'].describe())
    plt.figure(figsize=(10,6))
    sns.histplot(df['Price_PKR'], bins=30, color='mediumpurple')
    plt.title('Price Distribution')
    plt.xlabel('Price (PKR)')
    plt.ylabel('Number of Listings')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(x=df['Price_PKR'], color='gold')
    plt.title('Price Distribution (Box Plot)')
    plt.xlabel('Price (PKR)')
    plt.tight_layout()
    plt.show()
price()
def city_wise():
    print("========================================================================")
    print("City-wise Analysis")
    print("========================================================================")
    print(df['City'].value_counts())
    plt.figure(figsize=(10,7))
    sns.countplot(data=df, y='City', order=df['City'].value_counts().index, palette='coolwarm')
    for i in range(len(df['City'].value_counts())):
        plt.text(df['City'].value_counts().iloc[i], i, str(df['City'].value_counts().iloc[i]), ha='left', va='center')
    plt.title('Number of Listings by City')
    plt.xlabel('Count')
    plt.ylabel('City')
    plt.tight_layout()
    plt.show()
city_wise()

# df.to_excel(r"PakWheels_Used_Car_Dataset.xlsx", index=False)