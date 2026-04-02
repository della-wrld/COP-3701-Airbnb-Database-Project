import pandas as pd
import numpy as np
import random 
from datetime import datetime, timedelta

# --- STEP 1: LOAD RAW DATA ---
# Using the standard filename from the project folder
df = pd.read_csv('AB_NYC_2019.csv')

# --- STEP 2: HOSTS TABLE ---
# Getting unique hosts so we don't have duplicates
hosts = df[['host_id', 'host_name']].drop_duplicates(subset=['host_id'])

# Simple loop to assign Superhost status
superhost_list = []
for _ in range(len(hosts)):
    if random.random() < 0.2:
        superhost_list.append(True)
    else:
        superhost_list.append(False)

hosts['is_superhost'] = superhost_list
hosts.to_csv('data/hosts.csv', index=False)
print("Finished hosts.csv...")

# --- STEP 3: LISTINGS TABLE ---
# Renaming columns to match the SQL schema exactly
listings = df[['id', 'name', 'room_type', 'latitude', 'longitude', 'host_id']]
listings.columns = ['listing_id', 'property_name', 'room_type', 'latitude', 'longitude', 'host_id']
listings.to_csv('data/listings.csv', index=False)
print("Finished listings.csv...")

# --- STEP 4: USERS TABLE ---
# Project requirement: at least 100 users (making 150)
num_users = 150
user_ids = range(1001, 1001 + num_users)
user_rows = []

for u_id in user_ids:
    email_val = "user_" + str(u_id) + "@gmail.com"
    phone_val = "555-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))
    days_offset = random.randint(0, 365)
    reg_date = datetime(2023, 1, 1) + timedelta(days=days_offset)
    
    user_rows.append([u_id, email_val, phone_val, reg_date.date()])

users = pd.DataFrame(user_rows, columns=['user_id', 'email', 'phone_number', 'registration_date'])
users.to_csv('data/users.csv', index=False)
print("Finished users.csv...")

# --- STEP 5: PROFILES TABLE ---
# Linking a bio to each user
profile_rows = []
for u_id in user_ids:
    p_id = u_id + 4000
    bio = "Hi! I am traveler " + str(u_id) + ". I love exploring NYC."
    profile_rows.append([p_id, bio, u_id])

profiles = pd.DataFrame(profile_rows, columns=['profile_id', 'bio_text', 'user_id'])
profiles.to_csv('data/profiles.csv', index=False)
print("Finished profiles.csv...")

# --- STEP 6: BOOKINGS TABLE ---
num_bookings = 200
all_listings = listings['listing_id'].tolist()
booking_rows = []

for i in range(num_bookings):
    b_id = 9001 + i
    check_in = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 300))
    price = round(random.uniform(55.0, 475.0), 2)
    request = random.choice(["None", "Late arrival", "Extra towels", "High floor"])
    
    # Selecting random IDs from our other lists
    u_ref = random.choice(user_ids)
    l_ref = random.choice(all_listings)
    
    booking_rows.append([b_id, check_in.date(), price, request, u_ref, l_ref])

bookings = pd.DataFrame(booking_rows, columns=['booking_id', 'check_in', 'total_price', 'special_requests', 'user_id', 'listing_id'])
bookings.to_csv('data/bookings.csv', index=False)
print("Finished bookings.csv...")

# --- STEP 7: SEASONAL RATES ---
# Multiplier for every listing to show pricing changes
rate_rows = []
for index, row in listings.iterrows():
    rate_id = 80001 + index
    season = random.choice(['Summer Peak', 'Winter Off-Peak', 'Spring Break'])
    mult = round(random.uniform(0.8, 1.5), 2)
    rate_rows.append([rate_id, season, mult, row['listing_id']])

seasonal_rates = pd.DataFrame(rate_rows, columns=['rate_id', 'season_name', 'price_multiplier', 'listing_id'])
seasonal_rates.to_csv('data/seasonal_rates.csv', index=False)

print("\nPre-processing finally complete!")