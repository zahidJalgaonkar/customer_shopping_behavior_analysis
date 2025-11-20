import pandas as pd
import numpy as np

# ===========================================
# Load Dataset
# ===========================================
df = pd.read_csv("customer_shopping_behavior.csv")
print(df.info())
print(df.describe())

# ===========================================
# Handle Missing Values in 'Review Rating'
# Fill missing ratings with the median rating of each category
# ===========================================
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))

# ===========================================
# Clean and Standardize Column Names
# Convert to lowercase and replace spaces with underscores
# ===========================================
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Rename specific columns for clarity
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

# ===========================================
# Create 'age_group' Column Using Quantile Bins
# Divide customers into 4 age groups
# ===========================================
age_labels = ["Young Adult", "Adult", "Middle-aged", "Senior"]
df["age_group"] = pd.qcut(df["age"], q=4, labels=age_labels)

print("Sample Age Grouping:")
print(df[["age", "age_group"]].head(10))
print("-" * 50)

# ===========================================
# Create 'purchase_frequency_days' Column
# Convert frequency categories into equivalent number of days
# ===========================================
print("Unique Frequency Values:")
print(df["frequency_of_purchases"].unique())

frequency_mapping = {
    "Fortnightly": 14,
    "Bi-Weekly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Every 3 Months": 90,
    "Annually": 365
}

df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

print("\nMapped Purchase Frequency (Days):")
print(df[["frequency_of_purchases", "purchase_frequency_days"]].head())
print("-" * 50)

# ===========================================
# Compare 'discount_applied' and 'promo_code_used'
# If both columns are identical, keep only one
# ===========================================
same_discounts = (df["discount_applied"] == df["promo_code_used"]).all()
print(f"Are 'discount_applied' and 'promo_code_used' the same? {same_discounts}")

if same_discounts:
    df.drop("promo_code_used", axis=1, inplace=True)
    print("'promo_code_used' column removed since both were identical.")
else:
    print("Columns are different — keeping both.")

print("-" * 50)
print("Final Columns:")


from sqlalchemy import create_engine

# Replace placeholders with your actual details
username="postgres"# default user
password = "zahid123" 
host ="localhost"
port="5432"
database="customer_behavior"
engine= create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
# Step 2:load DataFrame into PostgresQl
table_name="customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
