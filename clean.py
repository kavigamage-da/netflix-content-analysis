import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print("Original rows:", len(df))

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

# Keep only Movie and TV Show
df = df[df['type'].isin(['Movie', 'TV Show'])]

# Remove Unknown countries
df = df[df['country'] != 'Unknown']

# Remove rows with no year_added
df = df[df['year_added'].notna()]

# Remove years before 2008
df = df[df['year_added'] >= 2008]

# Save
df.to_csv("netflix_clean.csv", index=False)
print("Clean rows:", len(df))
print("\nType values:", df['type'].value_counts().to_dict())
print("Year range:", int(df['year_added'].min()), "-", int(df['year_added'].max()))
print("Countries sample:", df['country'].value_counts().head(5).to_dict())
print("\n✅ All clean!")