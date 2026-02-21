# COP-3701-Airbnb-Database-Project
# NYC Rental Marketplace Database
* **Domain:** Real Estate Tech and Data Engineering
* **High-Level Goal:** Develop a database backend for the airbnb rental marketplace that will implement dynamic pricing logic and optimized geographic search capabilities. 
## Project Scope
* **Relational Database Architecture:** Normalizing raw CSV data into structured tables (Listings, Hosts, and Pricing) to ensure data integrity.
* **Dynamic Pricing Views:** Implementation of SQL views that calculate "Optimal Market Rates" based on current listing availability and neighborhood demand metrics.
* **Seasonal Trend Analysis:** Developing analytical queries to track price volatility across the 12-month calendar, identifying "high-season" trends for each NYC borough.
* **Indexed Geolocation Queries:** Utilizing spatial indexing to enable rapid proximity-based searches, allowing users to find rentals within a specific radius of NYC landmarks.

## Target Users
* **Marketplace Operators:** Who need to monitor the health and pricing parity of listings across different NYC neighborhoods.
* **Rental Hosts:** Who require data-driven "suggested pricing" to remain competitive throughout the year.
* **Travelers/End-Users:** Who need to find accommodations based on specific geographic proximity and budget constraints.

## Data Sources
* **Primary Source:** [New York City Airbnb Open Data (2019)](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
* **Format:** CSV (`AB_NYC_2019.csv`)
* **Description:** This dataset provides approximately 49,000 observations of listing activity in NYC. Key attributes include geographical coordinates, neighborhood groups (boroughs), room types, pricing, and review metrics.

## Database Application Proposal
This application is a comprehensive rental marketplace engine designed to manage short-term accommodations in New York City. Beyond simple data storage, the system facilitates user bookings, host management, and dynamic seasonal pricing. 

**Unique Technical Aspects:**
* **Associative Booking Logic:** Handles complex many-to-many relationships between guests and properties.
* **Weak Entity Pricing:** Implements `Seasonal_Rates` that exist only in relation to specific listings to support dynamic market analysis.
* **User Group Segregation:** Differentiates between 'Hosts' (service providers) and 'Travelers' (consumers).
