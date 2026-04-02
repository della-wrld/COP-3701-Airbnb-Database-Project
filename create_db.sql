DROP TABLE IF EXISTS seasonal_rates;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS hosts;

CREATE TABLE hosts (
    host_id INT PRIMARY KEY,
    host_name VARCHAR(255) NOT NULL,
    is_superhost BOOLEAN DEFAULT FALSE
);

CREATE TABLE users(
    user_id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(50),
    registration_date DATE NOT NULL
);

CREATE TABLE profiles(
    profile_id INT PRIMARY KEY,
    bio_text TEXT,
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE listings(
    listing_id INT PRIMARY KEY,
    property_name VARCHAR(255),
    room_type VARCHAR(50),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    host_id INT,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id)
);

CREATE TABLE bookings(
    booking_id INT PRIMARY KEY,
    check_in DATE NOT NULL,
    total_price DECIMAL(10,2),
    special_requests TEXT,
    user_id INT,
    listing_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);

CREATE TABLE seasonal_rates(
    rate_id INT PRIMARY KEY,
    season_name VARCHAR(50),
    price_multiplier DECIMAL(3,2),
    listing_id INT,
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);