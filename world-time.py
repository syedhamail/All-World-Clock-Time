import streamlit as st
import pytz
import pycountry
from datetime import datetime

# Get list of all countries and their respective timezones
country_timezones = {country.name: pytz.country_timezones.get(country.alpha_2, []) for country in pycountry.countries}

st.title("🌍 All World Clock Time")

# Country selection
selected_country = st.selectbox("Select a country:", list(country_timezones.keys()))

# Get current time for selected country
timezones = country_timezones.get(selected_country, [])
if timezones:
    tz = pytz.timezone(timezones[0])  # Take the first timezone if multiple exist
    current_time = datetime.now(tz).strftime("%Y-%m-%d %I:%M:%S %p")  # 12-hour format with AM/PM
    
    # Display clock and time
    st.markdown(f"## 🕰️ {selected_country} Current Time")
    st.markdown(f"### {current_time}")
else:
    st.markdown("## ❌ No timezone found for this country")
