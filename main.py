import streamlit as st

st.set_page_config(page_title="WonderLand Zoo", page_icon="🦁", layout="centered")

prices = {"Egyptian" : 120, "Tourist": 25}

def calculate_ticket(nationality, age):
    global prices
    if age < 2:
        dis = 1
    elif age < 6:
        dis = 0.5
    elif age < 13:
        dis = 0.25
    elif age < 20:
        dis = 0.15
    else:
        dis = 0.1
    orig = prices[nationality]
    dis_p = f"{int(dis * 100)} %"
    f = orig * (1 - dis)
    return f, orig, dis_p
nationalities = ["Egyptian", "Tourist"]

st.title("Welcome to WonderLand Zoo!")
nation = st.selectbox("Choose Nation", options=nationalities)
if nation == "Tourist":
    curreny = st.number_input("1 dollar to egp =", min_value=1, step=1)
    prices["Tourist"] = 25 * curreny
age = st.number_input("Enter your age", step=1)

button = st.button("Calculate Ticket", type="primary")
if button:
    if age < 0:
        st.error("Enter positive/neutral age")
    else:    
        final, org, dis_per = calculate_ticket(nation, age)
        data = {
            "Information Needed": ["Nationalty", "Age"],
            "User's Input" : [nation, age],
            "Final Price Data": ["Original ticket price", "The Discount Applied"],
            "Prices and Discounts": [org, dis_per]
            }
        st.dataframe(data)
        st.success(f"🎉 Final Price: {int(final)} EGP 🎉")
