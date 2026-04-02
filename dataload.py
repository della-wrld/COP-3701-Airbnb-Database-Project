import sqlite3
import pandas as pd
import os

# 1. Setup the connection to my new database
db_file = 'nyc_airbnb.db'
print(f"Starting the data load into {db_file}...")

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 2. Running my SQL file to create all the empty tables first
try:
    with open('create_db.sql', 'r') as f:
        sql_commands = f.read()
    cursor.executescript(sql_commands)
    print("Schema created successfully from create_db.sql.")
except Exception as e:
    print(f"Had an issue creating tables: {e}")

# 3. List of the CSVs I generated in the /data folder
tables_to_load = ['hosts', 'users', 'profiles', 'listings', 'bookings', 'seasonal_rates']

for table in tables_to_load:
    csv_path = f'data/{table}.csv'
    
    if os.path.exists(csv_path):
        # Reading the CSV and pushing it to the SQL table
        temp_df = pd.read_csv(csv_path)
        temp_df.to_sql(table, conn, if_exists='append', index=False)
        print(f"Successfully loaded {len(temp_df)} rows into the {table} table.")
    else:
        print(f"Oops: {csv_path} was not found. Skipping it.")

# 4. Save and wrap up
conn.commit()
conn.close()
print("\nAll done! The database population is complete.")