import pandas as pd

# Sample data for top 5 states based on police capacity metrics (mock data for demonstration)
data = {
    "State": ["Tamil Nadu", "Kerala", "Maharashtra", "Karnataka", "Gujarat"],
    "Police per Lakh Pop.": [215, 210, 190, 195, 200],
    "% Vacancies Filled": [92, 95, 85, 88, 90],
    "Budget per Officer (₹ in Lakh)": [3.2, 2.9, 3.5, 3.1, 3.3],
    "Training Infra Score (out of 10)": [8.5, 8.2, 7.5, 8.0, 7.8],
    "Equipment Modernization (out of 10)": [9.0, 8.0, 8.5, 7.8, 8.6],
    "Crime Clearance Rate (%)": [75, 78, 70, 72, 74],
    "Community Policing (out of 10)": [9.5, 8.5, 7.8, 8.0, 7.5],
    "Response Time Score (out of 10)": [8.0, 8.2, 7.0, 7.5, 7.8]
}

df = pd.DataFrame(data)

# Normalize and compute weighted score
from sklearn.preprocessing import MinMaxScaler

# Assign weights to each metric
weights = {
    "Police per Lakh Pop.": 0.20,
    "% Vacancies Filled": 0.15,
    "Budget per Officer (₹ in Lakh)": 0.15,
    "Training Infra Score (out of 10)": 0.10,
    "Equipment Modernization (out of 10)": 0.10,
    "Crime Clearance Rate (%)": 0.15,
    "Community Policing (out of 10)": 0.10,
    "Response Time Score (out of 10)": 0.05
}

# Normalize numeric data
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df.drop(columns=["State"]))
normalized_df = pd.DataFrame(normalized_data, columns=df.columns[1:])

# Apply weights and calculate final score
df["Composite Score"] = normalized_df.mul(pd.Series(weights)).sum(axis=1)

# Rank the states based on score
df["Rank"] = df["Composite Score"].rank(ascending=False).astype(int)
df = df.sort_values(by="Composite Score", ascending=False)

df.reset_index(drop=True, inplace=True)
df[["Rank", "State", "Composite Score"]] + df.drop(columns=["State", "Composite Score"])
