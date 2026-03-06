import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Clean dates
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Fix missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# Fix type column — keep only Movie and TV Show
df = df[df['type'].isin(['Movie', 'TV Show'])]

# Save clean file
df.to_csv("netflix_clean.csv", index=False)
print("✅ Done! Rows:", len(df))
print("Types:", df['type'].value_counts())