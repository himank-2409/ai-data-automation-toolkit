import pandas as pd
import google.generativeai as genai

# insert your API key here
genai.configure(api_key="AIzaSyBu5MLv1JMCwVmwDT04ho8H3w3-y99MQtM")

file_name = "data.xlsx"  # change this to your file name

if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
elif file_name.endswith(".xlsx"):
    df = pd.read_excel(file_name, engine="openpyxl")

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

stats = {
    "records": len(df),
    "missing_values": int(df.isnull().sum().sum())
}

if "total_spent" in df.columns:
    stats["total_revenue"] = float(df["total_spent"].sum())
    stats["average_spend"] = float(df["total_spent"].mean())

#prompttype = input("Enter the type of insight you want (e.g. 'trends', 'recommendations', 'short', 'detailed' etc.): ").strip().lower()
prompt = f"""
Write a short business insight summary for this dataset:

{stats}
"""

model = genai.GenerativeModel("gemini-3.1-pro-preview")
print("\nGenerating AI summary...")
response = model.generate_content(prompt)

print("\nAI Summary:\n")
print(response.text)

with open("ai_summary.txt", "w") as f:
    f.write(response.text)

print("\nAI summary saved as ai_summary.txt")
e = input("\nPress Enter to exit...")
exit()
