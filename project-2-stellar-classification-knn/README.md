# Project 2: Stellar Object Classification using KNN

A K-Nearest Neighbors classifier that identifies whether an astronomical object is a **Star**, **Galaxy**, or **Quasar (QSO)**, using real observational data from the Sloan Digital Sky Survey (SDSS17).

## Dataset
[Stellar Classification Dataset SDSS17](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17) — ~100,000 real space objects with photometric and spectroscopic measurements.

## Features Used
- `u`, `g`, `r`, `i`, `z` — brightness measured through 5 different light filters
- `redshift` — how much the object's light has stretched due to cosmic expansion (the strongest predictor — high redshift = distant quasar, near-zero = nearby star)

Equipment/ID metadata (object ID, run ID, plate, fiber ID, etc.) was dropped — these describe *how* the observation was taken, not *what* the object physically is.

## Pipeline
1. Load and explore the dataset
2. Drop non-predictive ID/metadata columns
3. Scale numeric features with `StandardScaler` (critical for KNN's distance-based approach)
4. Stratified train/test split
5. Train a KNN classifier
6. Evaluate with accuracy, classification report, and confusion matrix
7. Tune K (tested 1–20) to find the best-performing value

## Tech Used
Python 3.x, pandas, scikit-learn, matplotlib, seaborn, Streamlit

## How to Run

**Notebook:**
```bash
pip install -r requirements.txt
jupyter notebook project2_sdss_knn.ipynb
```

**Live interactive demo:**

Deployed Website: https://project-2-stellar-classification-knn-hvrhfu4hdppwzwv8dca6b9.streamlit.app

Then adjust the sliders (u, g, r, i, z, redshift) and watch the model classify the object live, with a probability breakdown across all 3 classes.

## Results
- Best K: 8
- Test Accuracy: 96.69%

## What I Learned
- Why feature scaling is essential specifically for distance-based algorithms like KNN
- How to identify and drop identifier/metadata columns that carry no real predictive signal
- Choosing K through systematic testing rather than guessing
- Turning a notebook model into an interactive demo with Streamlit

## Possible Future Improvements
- Test dropping `redshift` alone to measure how much that one feature drives accuracy
- Compare against Decision Tree / Logistic Regression on the same data
- Visualize per-class distributions of each filter to see which separates classes best
