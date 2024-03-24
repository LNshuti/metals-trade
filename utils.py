import pandas as pd
import sqlite3

def load_rankings(file_path):
    # Load the rankings.dta file into a pandas DataFrame
    rankings_df = pd.read_stata(file_path)
    return rankings_df

def print_descriptive_statistics(rankings_df):
    # Print simple descriptive statistics of the DataFrame
    print(rankings_df.describe())

def write_to_sqlite(rankings_df, db_path):
    # Write the DataFrame to a SQLite database
    conn = sqlite3.connect(db_path)
    rankings_df.to_sql('rankings', conn, if_exists='replace', index=False)
    conn.close()

# File paths
file_path = 'data/rankings.dta'
db_path = 'data/processed/rankings.db'

# Load the rankings file
rankings_df = load_rankings(file_path)

# Print descriptive statistics
print_descriptive_statistics(rankings_df)

# Write to SQLite database
write_to_sqlite(rankings_df, db_path)