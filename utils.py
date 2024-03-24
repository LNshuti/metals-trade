import pandas as pd
import sqlite3

def load_hs_product(file_path):
    # Load the hs_product.dta file into a pandas DataFrame
    hs_product_df = pd.read_stata(file_path)
    return hs_product_df

def print_descriptive_statistics(hs_product_df):
    # Print simple descriptive statistics of the DataFrame
    print(hs_product_df.describe())

def write_to_sqlite(hs_product_df, db_path):
    # Write the DataFrame to a SQLite database
    conn = sqlite3.connect(db_path)
    hs_product_df.to_sql('hs_product', conn, if_exists='replace', index=False)
    conn.close()

# File paths
file_path = 'data/hs_product.dta'
db_path = 'data/processed/hs_product.db'

# Load the hs_product file
hs_product_df = load_hs_product(file_path)

# Print descriptive statistics
print_descriptive_statistics(hs_product_df)

# Write to SQLite database
write_to_sqlite(hs_product_df, db_path)
