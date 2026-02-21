# Database ER Design

## Overview
This ER diagram models an Airbnb management database for New York City listings.

## User Groups
- Hosts
- Guests
- Platform Administrators
- Data Analysts

## Entities
- Host (Strong Entity)
- Listing (Strong Entity)
- Neighborhood (Strong Entity)
- Guest (Strong Entity)
- Review (Weak Entity)
- Booking (Associative Entity)

## Relationship Types
- One-to-One: Listing ↔ AvailabilityCalendar
- One-to-Many: Host → Listing
- One-to-Many: Listing → Review
- Many-to-Many: Guest ↔ Listing (via Booking)

## Attribute Requirements
- Identifier Attribute: listing_id
- Mandatory Attribute: host_name
- Optional Attribute: review_comment
- Single-value Attribute: price

## ER Diagram
![ER Diagram](er_diagram.png)
