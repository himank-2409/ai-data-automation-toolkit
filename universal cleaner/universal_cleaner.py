import pandas as pd
import os
import re

file_name = "customer.xlsx"  # input("Enter dataset file name (CSV or Excel): ")

if not os.path.exists(file_name):
    print("File not found.")
    exit()

# detect file type
if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
elif file_name.endswith(".xlsx"):
    df = pd.read_excel(file_name)
else:
    print("Unsupported file type")
    exit()

print("\nDataset loaded.")
print("Original shape:", df.shape)

# normalize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# remove duplicates
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates(subset=["email_address"])

# fill missing values
missing_before = df.isnull().sum().sum()
df = df.fillna("unknown")

# phone cleaning (if column exists)
if "phone" in df.columns:
    def clean_phone(phone):
        digits = re.sub(r"\D", "", str(phone))
        return digits
    df["phone"] = df["phone"].apply(clean_phone)

# output file
output_file = "cleaned_" + file_name
df.to_csv(output_file, index=False)

print("\nCleaning Report")
print("Duplicates removed:", duplicate_count)
print("Missing values fixed:", missing_before)
print("Final shape:", df.shape)

print("\nClean dataset saved as:", output_file)