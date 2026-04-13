import streamlit as st
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("Match_Predictor.pkl")
columns = joblib.load("columns.pkl")

st.title("Cricket Match Winner Prediction")

# Inputs
team1 = st.selectbox("Team 1", ["India", "Australia", "England", "Pakistan", "South Africa", "New Zealand"])
team2 = st.selectbox("Team 2", ["India", "Australia", "England", "Pakistan", "South Africa", "New Zealand"])

toss_winner = st.selectbox("Toss Winner", ["India", "Australia", "England", "Pakistan", "South Africa", "New Zealand"])
toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

overs = st.slider("Overs", 10, 50)
run_rate = st.slider("Run Rate", 1, 15)
target = st.slider("Target", 50, 400)

# Create empty dataframe with all columns
input_df = pd.DataFrame(columns=columns)
input_df.loc[0] = 0

# Fill numeric values
if "overs" in input_df.columns:
    input_df["overs"] = overs

if "run_rate" in input_df.columns:
    input_df["run_rate"] = run_rate

if "target" in input_df.columns:
    input_df["target"] = target

# Fill categorical (one-hot encoding)
if f"team1_{team1}" in input_df.columns:
    input_df[f"team1_{team1}"] = 1

if f"team2_{team2}" in input_df.columns:
    input_df[f"team2_{team2}"] = 1

if f"toss_winner_{toss_winner}" in input_df.columns:
    input_df[f"toss_winner_{toss_winner}"] = 1

if f"toss_decision_{toss_decision}" in input_df.columns:
    input_df[f"toss_decision_{toss_decision}"] = 1

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success(f"{team1} will WIN!")
    else:
        st.error(f"{team2} will LOSE!")