"""Starter dashboard for Grade 10 Unit 7.  Run:  streamlit run app/air_dashboard.py

Uses the SYNTHETIC air-quality table. Replace DATA_FILE with the real file (after checking its licence)
and keep the source note honest.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

HERE = Path(__file__).resolve()
DATA_FILE = next(
    p / "datasets" / "kathmandu-air-quality" / "clean" / "air_daily_synthetic.csv"
    for p in HERE.parents
    if (p / "datasets" / "kathmandu-air-quality" / "clean" / "air_daily_synthetic.csv").exists()
)

st.set_page_config(page_title="Air in my city", layout="centered")
st.title("Air in my city: daily PM2.5")
st.caption("SYNTHETIC practice data - invented numbers. Source and limits are at the bottom.")


@st.cache_data
def load() -> pd.DataFrame:
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    df["pm25"] = df["pm25"].replace(-999, np.nan)  # -999 is a sensor error code
    return df


air = load()
years = sorted(air["date"].dt.year.unique())
year = st.sidebar.selectbox("Year", years)
window = st.sidebar.slider("Smoothing window (days)", 1, 30, 7)

view = air[air["date"].dt.year == year].set_index("date")
view = view.assign(smooth=view["pm25"].rolling(window, min_periods=1).mean())

left, right = st.columns(2)
left.metric("Mean PM2.5 (ug/m3)", f"{view['pm25'].mean():.1f}")
right.metric("Missing days", int(view["pm25"].isna().sum()))

st.line_chart(view[["pm25", "smooth"]])

st.markdown(
    "**Source:** synthetic table from `datasets/kathmandu-air-quality`. "
    "**Limits:** one station; missing days; invented numbers. "
    "**Credit:** Data Science Nepal (CC BY 4.0)."
)
