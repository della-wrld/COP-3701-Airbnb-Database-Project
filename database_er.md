# Final Normalizized Relational Schema

## Overview
The following tables represent the logical design of the NYC Rental Marketplace. This schema has been normalized to Boyce-Codd Normal Form to ensure that every determinant is a candidate key, and eliminates data redundancy. 

## Table: Hosts
- host_id[PK] (identifier)
- host_name (Mandatory)
- is_superhost(Optional)
  
## Table: Users
- user_id[PK] (Identifier)
- email[Unique] (Mandatory)
- phone_number (Optional)
- registration_date (Single_value)

## Table: Profiles
- profile_id[PK] (Identifier)
- bio_text (Optional)
- user_id[FK] (1:1 with Users)

## Table : Listings
- listing_id [PK] (Identifier)
- property_name (Mandatory)
- room_type (Single_value)
- latitude (Mandatory)
- longitude (Mandatory)
- host_id [FK] (Many-to-One with Hosts)

## Table: Bookings
- booking_id [PK] (Identifier)
- check_in (Mandatory)
- total_price (Mandatory)
- special_requests (Optional)
- user_id [FK] (Linking to Travelers)
- listing_id [FK] (Linking to Listings)

## Table: Seasonal_Rates (Weak Entity)
- rate_id [PK] (Identifier)
- season_name (Single-value)
- price_multiplier (Mandatory)
- listing_id [FK] (Identified by Listing)

## NYC Rental Relational Schema
<img width="1140" height="506" alt="NYC Rental Relational Schema" src="https://github.com/user-attachments/assets/9509d3b0-490c-4a80-b113-a59912d0da65" />


