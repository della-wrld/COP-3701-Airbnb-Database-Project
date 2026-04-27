import streamlit as st
import oracledb
import pandas as pd

# Path to your Instant Client (Required for Thick Mode)
# Step 3 for your README: Update this path to match your computer!
LIB_DIR = r"C:\oracle\instantclient_21_3"

# Update these with your specific database credentials
DB_USER = "your_username"
DB_PASS = "your_password"
DB_DSN = "localhost:1521/xe"


@st.cache_resource
def init_db():
    try:
        oracledb.init_oracle_client(lib_dir=LIB_DIR)
    except Exception as e:
        pass


init_db()


def get_connection():
    return oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)


# --- User Interface ---
st.title("AirBNB NYC Rental Marketplace")
st.subheader("Database Management & Analysis Tool")

menu = ["Read from:", "Join:", "Check Listings:", "Booking Dates:", "Check Seasonal Discount:"]
choice = st.sidebar.selectbox("Select Action", menu)

# --- Feature 1: Read from Table ---
if choice == "Read from:":
    st.write("### View Table Contents")
    table_list = ["bookings", "hosts", "listings", "profiles", "seasonal_rates", "users"]
    selected_table = st.sidebar.selectbox("Select a table", table_list)
    columns = st.text_input("Enter column names (use '*' for all or separate by commas)", value="*")

    if st.button("Display Data"):
        try:
            conn = get_connection()
            query = f"SELECT {columns} FROM {selected_table}"
            df = pd.read_sql(query, conn)
            st.dataframe(df)
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# --- Feature 2: Table Joins ---
elif choice == "Join:":
    st.write("### Relational Data Join")
    st.write("Example: Joining Listings and Hosts to see ownership.")
    if st.button("Run Join Query"):
        try:
            conn = get_connection()
            query = """
                SELECT l.property_name, l.room_type, h.host_name, h.is_superhost 
                FROM listings l 
                JOIN hosts h ON l.host_id = h.host_id
                FETCH FIRST 50 ROWS ONLY
            """
            df = pd.read_sql(query, conn)
            st.table(df)
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# --- Feature 3: Seasonal Discounts ---
elif choice == "Check Seasonal Discount:":
    st.write("### Dynamic Pricing Calculator")
    st.write("Check how seasonal multipliers affect listing prices.")

    # This logic matches your 'Weak Entity' proposal
    if st.button("Analyze Current Rates"):
        try:
            conn = get_connection()
            query = """
                SELECT l.property_name, s.season_name, s.price_multiplier 
                FROM listings l 
                INNER JOIN seasonal_rates s ON l.listing_id = s.listing_id
                FETCH FIRST 20 ROWS ONLY
            """
            df = pd.read_sql(query, conn)
            st.dataframe(df)
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")