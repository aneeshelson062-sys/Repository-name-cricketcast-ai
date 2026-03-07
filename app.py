import streamlit as st

st.set_page_config(
    page_title="CricketCast AI",
    page_icon="🏏",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0B1F3A;
}

/* Main content container */
.block-container{
background: #142B4D;
padding: 60px;
border-radius: 15px;
max-width: 1100px;
margin: auto;
box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
}

/* Main title */
h1{
font-size:60px !important;
color:#00D4FF !important;
font-weight:bold;
}

/* Subtitle */
h3{
font-size:35px !important;
color:#FACC15 !important;
}

/* Paragraph text */
p{
font-size:20px !important;
color:#E5E7EB !important;
}

/* Features list */
li{
font-size:20px !important;
color:#E5E7EB !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
background:#06142B;
}

/* Sidebar text */
[data-testid="stSidebar"] *{
color:white !important;
font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# BIG LOGO
st.image("logo.png", width=400)

# WEBSITE TITLE
st.title("CricketCast AI")

# TAGLINE
st.subheader("Smart IPL Score Prediction System")

st.write(
"""
This platform uses **Deep Learning (TensorFlow/Keras)** to predict the final
score of an IPL innings based on match conditions such as overs, wickets,
teams, and run rate.
"""
)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=450)
    st.title("CricketCast AI")
    st.subheader("Smart IPL Score Prediction System")

import streamlit as st

st.set_page_config(page_title="IPL Predictor", layout="wide")

st.title("🏏 IPL Score Prediction Dashboard")

st.markdown("""
Welcome to the **IPL Score Prediction System**.

This project uses **Deep Learning (TensorFlow/Keras)** to predict
the final score of an IPL innings based on match conditions.

### Features
- Predict IPL final score
- Score growth graph
- Feature importance visualization
- Match analytics
""")

st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Logo.svg/1200px-Indian_Premier_League_Logo.svg.png")


import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load trained model & scaler
model = tf.keras.models.load_model("ipl_model.h5", compile=False)
scaler = joblib.load("scaler.pkl")

st.title("🏏 IPL Score Prediction - Deep Learning Model")

teams = ["MI", "CSK", "RCB", "KKR", "SRH", "DC", "PBKS", "RR", "GT", "LSG"]
venues = ["Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad",
          "Delhi", "Mohali", "Jaipur", "Ahmedabad", "Lucknow"]

batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", teams)
venue = st.selectbox("Select Venue", venues)

overs = st.slider("Overs Completed", 1, 20)
wickets = st.slider("Wickets Lost", 0, 10)
run_rate = st.number_input("Current Run Rate", min_value=0.0)

team_dict = {team: i for i, team in enumerate(teams)}
venue_dict = {venue: i for i, venue in enumerate(venues)}

if st.button("Predict Score"):

    input_data = np.array([[team_dict[batting_team],
                            team_dict[bowling_team],
                            venue_dict[venue],
                            overs,
                            wickets,
                            run_rate]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.success(f"Predicted IPL Score: {int(prediction[0][0])} runs")




