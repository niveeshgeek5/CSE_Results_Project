import camelot
import pandas as pd

# Step 1: Extract tables from pages 8–11 (4th sem)
tables = camelot.read_pdf("RESULT APRIL 2025.pdf", pages="8-11", flavor="stream")

# Step 2: Combine all pages into one DataFrame
dfs = [t.df for t in tables]
df = pd.concat(dfs, ignore_index=True)

# Step 3: Rename columns properly
df.columns = ["Reg No", "Name", "CS3401", "CS3451", "CS3452", "CS3461", 
              "CS3481", "CS3491", "CS3492", "CS8491", "CS8492", "GE3451", 
              "MA8402", "NM1075"]

# Step 4: Keep only valid rows (those with register numbers)
df = df[df["Reg No"].str.contains("8204", na=False)]

# Step 5: Filter for 2023 batch only
df_2023 = df[df["Reg No"].str.contains("23")]

# Save for later use
df_2023.to_csv("sem4_results_2023.csv", index=False)
print(df_2023.head())