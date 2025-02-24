import pandas as pd
import matplotlib.pyplot as plt

sample_csv = "./root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal_first.csv"

### Option 1: Plot Only the Top N Studies
# Read the CSV file into a DataFrame
df = pd.read_csv(sample_csv)

# Rename columns for convenience
df = df.rename(columns={
    "attributes.samples-count": "samples_count",
    "id": "study_id"
})

# Convert samples_count to numeric (if needed)
df["samples_count"] = pd.to_numeric(df["samples_count"], errors='coerce')

# Sort the DataFrame by sample count in descending order and take the top 20
top20 = df.sort_values("samples_count", ascending=False).head(20)

# Plot a horizontal bar graph for better readability
plt.figure(figsize=(10, 8))
plt.barh(top20["study_id"], top20["samples_count"], color='skyblue')
plt.xlabel("Samples Count")
plt.title("Top 20 Studies by Sample Count")
plt.gca().invert_yaxis()  # Highest value on top
plt.tight_layout()
plt.savefig("Top_20_sample_size.svg")

### Option 2: Plot a Summary or Aggregated View
# Read the CSV file
df = pd.read_csv(sample_csv)

df = df.rename(columns={
    "attributes.samples-count": "samples_count",
    "id": "study_id"
})
df["samples_count"] = pd.to_numeric(df["samples_count"], errors='coerce')

# Create bins for sample counts
bins = [0, 100, 300, 500, 1000, df["samples_count"].max()]
labels = ["0-100", "101-300", "301-500", "501-1000", "1001+"]

df['count_bin'] = pd.cut(df['samples_count'], bins=bins, labels=labels, include_lowest=True)

# Plot a bar chart of the bins
bin_counts = df['count_bin'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
plt.bar(bin_counts.index.astype(str), bin_counts.values, color='salmon')
plt.xlabel("Samples Count Range")
plt.ylabel("Number of Studies")
plt.title("Distribution of Studies by Samples Count")
plt.tight_layout()
plt.savefig("Aggregate_sample_size.svg")

### Option 3: Plot All 320 Entries (Vertical Bars)
df = pd.read_csv(sample_csv)
df = df.rename(columns={
    "attributes.samples-count": "samples_count",
    "id": "study_id"
})
df["samples_count"] = pd.to_numeric(df["samples_count"], errors='coerce')

plt.figure(figsize=(10, 20))
plt.barh(df["study_id"], df["samples_count"], color='mediumseagreen')
plt.xlabel("Samples Count")
plt.title("Samples Count for 320 Studies")
plt.tight_layout()
plt.savefig("all_sample_size_count.svg")
