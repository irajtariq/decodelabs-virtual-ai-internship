"""
Project 2 — Live Demo App
Stellar Classification (Star / Galaxy / Quasar) using KNN
Made By: Iraj Tariq
"""

import os
import base64
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Always look for files right next to this script, regardless of
# what folder the app was launched from (fixes path issues on
# Streamlit Cloud / other deployment environments)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "star_classification.csv")
BG_IMAGE_PATH = os.path.join(SCRIPT_DIR, "background.jpg")


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Stellar Classifier", page_icon="🔭", layout="centered")


def set_background(image_path):
    if not os.path.exists(image_path):
        st.warning("Background image not found — running without it. "
                   "Add 'background.jpg' next to app.py to enable it.")
        return

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(5, 5, 20, 0.75), rgba(5, 5, 20, 0.75)),
                               url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


set_background(BG_IMAGE_PATH)

st.title("🔭 Stellar Object Classifier")
st.write(
    "A K-Nearest Neighbors model trained on real Sloan Digital Sky Survey (SDSS) data — "
    "classifies a space object as a **Star**, **Galaxy**, or **Quasar** based on its light measurements."
)


# -----------------------------
# Load data + train model (cached so it only runs once, not on every interaction)
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df[(df["u"] > -1000) & (df["g"] > -1000) & (df["r"] > -1000) & (df["i"] > -1000) & (df["z"] > -1000)]
    features = ["u", "g", "r", "i", "z", "redshift"]
    X = df[features]
    y = df["class"]
    return df, X, y, features


@st.cache_resource
def train_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)

    test_accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, scaler, test_accuracy


df, X, y, features = load_data()
model, scaler, test_accuracy = train_model(X, y)

st.success(f"Model trained on {len(df):,} real observations — test accuracy: **{test_accuracy:.1%}**")

st.divider()

# -----------------------------
# Interactive input section
# -----------------------------
st.subheader("Try it yourself")
st.write("Adjust the sliders to describe an object's light measurements, then see the model's live prediction.")

col1, col2 = st.columns(2)

with col1:
    u = st.slider("u (ultraviolet magnitude)", float(X["u"].min()), float(X["u"].max()), float(X["u"].median()))
    g = st.slider("g (green magnitude)", float(X["g"].min()), float(X["g"].max()), float(X["g"].median()))
    r = st.slider("r (red magnitude)", float(X["r"].min()), float(X["r"].max()), float(X["r"].median()))

with col2:
    i = st.slider("i (near-infrared magnitude)", float(X["i"].min()), float(X["i"].max()), float(X["i"].median()))
    z = st.slider("z (infrared magnitude)", float(X["z"].min()), float(X["z"].max()), float(X["z"].median()))
    redshift = st.slider("redshift", float(X["redshift"].min()), float(X["redshift"].max()), float(X["redshift"].median()))

# -----------------------------
# Prediction
# -----------------------------
input_df = pd.DataFrame([[u, g, r, i, z, redshift]], columns=features)
input_scaled = scaler.transform(input_df)

prediction = model.predict(input_scaled)[0]
probabilities = model.predict_proba(input_scaled)[0]
prob_df = pd.DataFrame({"Class": model.classes_, "Probability": probabilities}).sort_values(
    "Probability", ascending=False
)

st.divider()
st.subheader("Prediction")

emoji_map = {"STAR": "⭐", "GALAXY": "🌌", "QSO": "💫"}
st.markdown(f"### {emoji_map.get(prediction, '')} Predicted class: **{prediction}**")

fig, ax = plt.subplots(figsize=(5, 2.5))
ax.barh(prob_df["Class"], prob_df["Probability"], color="#FF1493")
ax.set_xlabel("Probability")
ax.set_xlim(0, 1)
for idx, val in enumerate(prob_df["Probability"]):
    ax.text(val + 0.02, idx, f"{val:.0%}", va="center")
st.pyplot(fig)

st.caption(
    "This app uses a K-Nearest Neighbors classifier trained on the SDSS17 stellar classification dataset. "
    "Built as part of the DecodeLabs AI Internship — Project 2 by Iraj Tariq."
)
