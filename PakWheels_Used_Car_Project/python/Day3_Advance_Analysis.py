import pandas as pd , matplotlib.pyplot as plt , seaborn as sns

df = pd.read_excel(r"PakWheels_Used_Car_Dataset.xlsx")

def correlation_analysis():
    print("========================================================================")
    print("Correlation Analysis")
    print("========================================================================")
    # sirf numeric columns lo
    numeric_cols = ['Price_PKR', 'Mileage_km', 'Manufacturing_Year', 'Engine_Capacity_cc']
    corr_matrix = df[numeric_cols].corr()
    print(corr_matrix)
    
    print("Manufacturing Year is the strongest driver of used car price, followed by Mileage (inverse relationship) and Engine Capacity.")
    plt.figure(figsize=(8,6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
# correlation_analysis()

def scatter_plots():
    print("========================================================================")
    print("Correlation Scatter Plots Analysis")
    print("========================================================================")
    print("Manufacturing Year is the strongest driver of used car price, followed by Mileage (inverse relationship) and Engine Capacity.")
    fig, axes = plt.subplots(1, 3, figsize=(18,5))

    sns.scatterplot(data=df, x='Mileage_km', y='Price_PKR', ax=axes[0], alpha=0.3)
    axes[0].set_title('Price vs Mileage')

    sns.scatterplot(data=df, x='Manufacturing_Year', y='Price_PKR', ax=axes[1], alpha=0.3)
    axes[1].set_title('Price vs Manufacturing Year')

    sns.scatterplot(data=df, x='Engine_Capacity_cc', y='Price_PKR', ax=axes[2], alpha=0.3)
    axes[2].set_title('Price vs Engine Capacity')

    plt.tight_layout()
    plt.show()
# scatter_plots()

def segment_price(price):
    if price <= 700000:
        return 'Budget'
    elif price <= 1800000:
        return 'Mid-range'
    elif price <= 3500000:
        return 'Premium'
    else:
        return 'Luxury'

df['Segment'] = df['Price_PKR'].apply(segment_price)
# print(df['Segment'].value_counts())

# plt.figure(figsize=(7,5))
# sns.countplot(data=df, x='Segment', order=['Mid-range','Budget','Premium','Luxury'], palette='Set2')
# for i in range(len(df['Segment'].value_counts())):
#     plt.text(i, df['Segment'].value_counts().iloc[i], str(df['Segment'].value_counts().iloc[i]), ha='center', va='bottom')
# plt.title('Vehicle Segments Distribution')
# plt.tight_layout()
# plt.show()

def segment_brand_distribution():
    for seg in ['Budget', 'Mid-range', 'Premium', 'Luxury']:
        print(f"\n===== {seg} Segment - Top Brands =====")
        print(df[df['Segment'] == seg]['Brand'].value_counts().head(5))
# segment_brand_distribution()


def segment_model_distribution():
    for seg in ['Budget', 'Mid-range', 'Premium', 'Luxury']:
        print(f"\n===== {seg} Segment - Top Models =====")
        print(df[df['Segment'] == seg]['Model'].value_counts().head(5))
# segment_model_distribution()

def segment_summary():
    summary = df.groupby('Segment').agg(
        Avg_Mileage=('Mileage_km', 'mean'),
        Avg_Manufacturing_Year=('Manufacturing_Year', 'mean'),
        Count=('Segment', 'count')
    ).reindex(['Budget', 'Mid-range', 'Premium', 'Luxury'])
    print(summary)
# segment_summary()

def top_brands_models():
    print("===== Top 10 Brands =====")
    print(df['Brand'].value_counts().head(10))

    print("\n===== Top 10 Models =====")
    print(df['Model'].value_counts().head(10))
# top_brands_models()

def preferences():
    print("===== Fuel Type Preference =====")
    print(df['Fuel_Type'].value_counts(normalize=True) * 100)

    print("\n===== Transmission Preference =====")
    print(df['Transmission'].value_counts(normalize=True) * 100)
# preferences()

def fastest_growing():
    df['Year_Group'] = df['Manufacturing_Year'].apply(lambda y: 'Older (2004-2014)' if y <= 2014 else 'Recent (2015-2025)')

    print("===== Fuel Type: Older vs Recent =====")
    print(pd.crosstab(df['Year_Group'], df['Fuel_Type'], normalize='index') * 100)

    print("\n===== Segment: Older vs Recent =====")
    print(pd.crosstab(df['Year_Group'], df['Segment'], normalize='index') * 100)
# fastest_growing()

def price_by_city():
    avg_price_city = df.groupby('City')['Price_PKR'].mean().sort_values(ascending=False)
    print(avg_price_city)

    plt.figure(figsize=(10,7))
    avg_price_city.plot(kind='barh', color='teal')
    for i, v in enumerate(avg_price_city):
        plt.text(v, i, f"{v:,.0f}", va='center', ha='left', color='black')
    plt.title('Average Price by City')
    plt.xlabel('Average Price (PKR)')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    # plt.show()
price_by_city()

def brand_by_city():
    top_brand_per_city = df.groupby('City')['Brand'].agg(lambda x: x.value_counts().idxmax())
    print(top_brand_per_city)
brand_by_city()