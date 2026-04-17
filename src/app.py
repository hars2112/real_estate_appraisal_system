import streamlit as st
import pandas as pd
import sqlite3
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Real Estate Appraisal System",
    page_icon="🏡",
    layout="wide"
)

# --- 2. SMART PATH LOGIC ---
# This ensures the database is found regardless of where you start the terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "processed", "propiedades_comparables.db"))

# --- 3. DATA LOADING FUNCTION ---
def load_data():
    if not os.path.exists(DB_PATH):
        st.error(f"❌ Database not found at: {DB_PATH}")
        st.info("Please run your Jupyter Notebook ETL script to generate the database.")
        return pd.DataFrame()
    
    try:
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT * FROM comparables"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Ensure numeric types for calculations
        numeric_cols = ['sale_price', 'bldg_size_sqft', 'price_per_sqft']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return pd.DataFrame()

# Load the data once
df = load_data()

# --- 4. SIDEBAR FILTERS ---
st.sidebar.header("🔍 Search Filters")

if not df.empty:
    # Region Filter
    all_regions = ["All"] + sorted(df['parish_region'].dropna().unique().tolist())
    selected_region = st.sidebar.selectbox("Select Parish/Region", all_regions)

    # Property Type Filter
    all_types = ["All"] + sorted(df['property_type'].dropna().unique().tolist())
    selected_type = st.sidebar.selectbox("Property Type", all_types)

    # Price Slider
    min_p = float(df['sale_price'].min())
    max_p = float(df['sale_price'].max())
    price_range = st.sidebar.slider("Price Range ($)", min_p, max_p, (min_p, max_p))

    # --- 5. FILTER LOGIC ---
    filtered_df = df.copy()

    if selected_region != "All":
        filtered_df = filtered_df[filtered_df['parish_region'] == selected_region]
    
    if selected_type != "All":
        filtered_df = filtered_df[filtered_df['property_type'] == selected_type]

    filtered_df = filtered_df[
        (filtered_df['sale_price'] >= price_range[0]) & 
        (filtered_df['sale_price'] <= price_range[1])
    ]

    # --- 6. MAIN INTERFACE ---
    st.title("🏡 Real Estate Appraisal Search Engine")
    st.markdown("---")

    # Display Metrics (KPIs)
    if not filtered_df.empty:
        m1, m2, m3 = st.columns(3)
        m1.metric("Properties Found", len(filtered_df))
        m2.metric("Avg. Sale Price", f"${filtered_df['sale_price'].mean():,.2f}")
        m3.metric("Avg. Price / SqFt", f"${filtered_df['price_per_sqft'].mean():,.2f}")

        # Display Table
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

        # Download Button
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📩 Export results to CSV",
            data=csv,
            file_name='appraisal_export.csv',
            mime='text/csv',
        )
    else:
        st.warning("No results found matching those filters. Try broadening your search.")

else:
    st.warning("Waiting for data...")
