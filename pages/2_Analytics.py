import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("📈 IPL Score Prediction Graph")

overs = np.arange(1,21)

scores = []

placeholder = st.empty()

for i in overs:
    score = i * np.random.randint(6,9)
    scores.append(score)

    fig, ax = plt.subplots()

    ax.plot(overs[:len(scores)], scores, marker="o", color="orange")
    ax.set_xlabel("Overs")
    ax.set_ylabel("Score")
    ax.set_title("Predicted Score Growth")

    placeholder.pyplot(fig)

    time.sleep(0.2)