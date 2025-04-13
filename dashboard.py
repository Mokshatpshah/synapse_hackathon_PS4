import streamlit as st
import requests

# Title and Intro
st.set_page_config(page_title="User Trait Inference Engine", layout="centered")
st.title(" User Trait Inference Engine")
st.markdown("Predict affluence level and consumer trait based on user behavior.")

# Input fields
age_group = st.selectbox("Select Age Group", ["Young Adult", "Adult", "Senior","Teen"])
tech_savviness = st.selectbox("Select Tech Savviness", ["Low", "Medium", "High"])
interests = st.text_input("Enter Interests (comma-separated)", "Tech,Finance")
device = st.selectbox("Select Device", ["Mobile", "Desktop"])
action = st.selectbox("Select Action", ["load_home", "scroll", "click_ad"])
items_added_to_cart = st.slider("Items Added to Cart", 0, 10, 1)
affluence_score = st.slider("Affluence Score", 0, 10, 5)

# Submit
if st.button("🔍 Predict"):
    # Prepare JSON payload
    payload = {
        "age_group": age_group,
        "tech_savviness": tech_savviness,
        "interests": interests,
        "device": device,
        "action": action,
        "items_added_to_cart": items_added_to_cart,
        "affluence_score": affluence_score
    }

    try:
        # Send request to FastAPI backend
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"🪙 Affluence Level: **{result['affluence_level']}**")
            st.info(f"🛍️ Consumer Trait: **{result['consumer_trait']}**")
        else:
            st.error(f"❌ Backend Error: {response.status_code}")
    except Exception as e:
        st.error(f"🔌 Failed to connect to backend: {e}")
