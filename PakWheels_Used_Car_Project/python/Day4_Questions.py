import pandas as pd , matplotlib.pyplot as plt , seaborn as sns

df = pd.read_excel(r"PakWheels_Used_Car_Dataset.xlsx")

def resale_value_analysis():
    current_year = 2026
    df['Age'] = current_year - df['Manufacturing_Year']

    # har brand ka: average price per year of age (higher = better value retention)
    resale = df.groupby('Brand').apply(
        lambda x: (x['Price_PKR'] / (x['Age'] + 1)).mean()
    ).sort_values(ascending=False)

    print(resale)
resale_value_analysis()