import streamlit as st
from data import tour_data

st.title("🌍 AI Virtual Tour Guide")

location = st.text_input("Enter Location (eg: Ooty)")

if st.button("Search"):
    key = location.lower()
    if key in tour_data:
        data = tour_data[key]

        st.subheader("🏨 Available Stays")
        for s in data["stays"]:
            st.write(f"{s['name']} – {s['price']}")

        st.subheader("🚗 Car Rentals")
        for c in data["cars"]:
            st.write(f"{c['name']} – {c['price']}")

        st.subheader("🏍️ Bike Rentals")
        for b in data["bikes"]:
            st.write(f"{b['name']} – {b['price']}")
    else:
        st.error("No data found for this location")
