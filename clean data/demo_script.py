import pandas as pd
import re

# Load dataset
file_name = input("Enter dataset file name (CSV): ")
df = pd.read_csv(file_name)

print("Original shape:", df.shape)
print("Original Data:")
print(df)

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["phone"] = df["phone"].fillna("unknown")
df["last_purchase"] = df["last_purchase"].fillna("no_purchase")

# Standardize phone numbers
def clean_phone(phone):
    if phone == "unknown":
        return phone
    digits = re.sub(r"\D", "", str(phone))
    return digits

df["phone"] = df["phone"].apply(clean_phone)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned shape:", df.shape)
print("Cleaned Data:")
print(df)
print("Cleaned file saved as cleaned_data.csv")
input("Press Enter to exit...")