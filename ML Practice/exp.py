# Required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = "SSC Result Trends in Bangladesh (20012025).csv"  # Ensure it's in the same folder
df = pd.read_csv("C:\\Users\\teama\\Downloads\\exam\\SSC Result Trends in Bangladesh (20012025).csv")


# Step 2: Preview the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Display column names
print("\nAvailable Columns:")
print(df.columns)

# Step 4: Set the target column for analysis
column = 'Pass_Rate'  # Change to 'GPA_5_Count' or 'Total_Examinees' if needed

# Step 5: Calculate mean, median, and mode
if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
    data = df[column].dropna()
    
    mean = data.mean()
    median = data.median()
    mode = data.mode().iloc[0] if not data.mode().empty else None

    print(f"\nStatistics for '{column}':")
    print(f"Mean   : {mean}")
    print(f"Median : {median}")
    print(f"Mode   : {mode}")
else:
    print(f"\nColumn '{column}' not found or is not numeric.")

# Step 6: Generate a line plot
x_col = 'Year'

# Convert year to string (optional, for cleaner x-axis)
df[x_col] = df[x_col].astype(str)

if x_col in df.columns and column in df.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[column], marker='o', linestyle='-', color='blue')
    plt.title(f"{column} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(column)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print(f"Cannot plot. Column '{x_col}' or '{column}' not found.")
