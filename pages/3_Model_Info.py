import streamlit as st

st.title("🧠 Model Information")

st.markdown("## Deep Learning Model for IPL Score Prediction")

st.write("""
This project uses a **Deep Neural Network (DNN)** to predict the final score of an IPL innings
based on match conditions.
""")

st.markdown("### ⚙️ Model Details")

st.write("""
- **Model Type:** Artificial Neural Network  
- **Framework:** TensorFlow / Keras  
- **Architecture:**  
  - Dense Layer (128 neurons, ReLU activation)  
  - Dense Layer (64 neurons, ReLU activation)  
  - Output Layer (1 neuron – predicted score)
""")

st.markdown("### 📊 Input Features")

st.write("""
The model uses the following inputs:

- Batting Team  
- Bowling Team  
- Venue  
- Overs Completed  
- Wickets Lost  
- Current Run Rate
""")

st.markdown("### 📈 Output")

st.write("""
The model predicts the **final total score** at the end of 20 overs.
""")

st.markdown("### 📏 Evaluation Metric")

st.write("""
- **MAE (Mean Absolute Error)** was used to evaluate the model performance.
""")

st.success("This system helps estimate the final score during a live IPL match.")