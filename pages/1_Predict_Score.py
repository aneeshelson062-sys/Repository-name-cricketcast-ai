import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load model and scaler
model = tf.keras.models.load_model("ipl_model.h5", compile=False)
scaler = joblib.load("scaler.pkl")

st.title("📊 IPL Score Prediction")

teams = ["MI","CSK","RCB","KKR","SRH","DC","PBKS","RR","GT","LSG"]

venues = ["Mumbai","Chennai","Bangalore","Kolkata","Hyderabad",
          "Delhi","Mohali","Jaipur","Ahmedabad","Lucknow"]

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
venue = st.selectbox("Venue", venues)

overs = st.slider("Overs Completed",1,20)
wickets = st.slider("Wickets Lost",0,10)

run_rate = st.number_input(
    "Current Run Rate",
    min_value=0.0,
    max_value=20.0,
    step=0.5
)

team_dict = {team:i for i,team in enumerate(teams)}
venue_dict = {venue:i for i,venue in enumerate(venues)}

if st.button("Predict Score"):

    input_data = np.array([[team_dict[batting_team],
                            team_dict[bowling_team],
                            venue_dict[venue],
                            overs,
                            wickets,
                            run_rate]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    predicted_score = int(prediction[0][0])

    st.success(f"Predicted IPL Score: {predicted_score} Runs")