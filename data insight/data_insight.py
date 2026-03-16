import pandas as pd

file_name = "data.csv"  # You can change this to your actual file name

# Load dataset
if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
elif file_name.endswith(".xlsx"):
    df = pd.read_excel(file_name, engine="openpyxl")
else:
    print("Unsupported file type")
    exit()

# Normalize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

print("\nDataset loaded successfully.")

# Basic stats
total_rows = len(df)

missing_values = df.isnull().sum().sum()

summary = f"""
DATASET SUMMARY REPORT
----------------------

Total records: {total_rows}

Total missing values: {missing_values}
"""

# Optional stats if columns exist
if "status" in df.columns:
    status_counts = df["status"].value_counts()
    summary += f"\nStatus distribution:\n{status_counts}\n"

if "total_spent" in df.columns:
    total_revenue = df["total_spent"].sum()
    avg_spend = df["total_spent"].mean()

    summary += f"""
Total revenue: {total_revenue}
Average spend per customer: {avg_spend:.2f}
"""

# Save report
with open("summary_report.txt", "w") as f:
    f.write(summary)

print(summary)
print("\nSummary report saved as summary_report.txt")