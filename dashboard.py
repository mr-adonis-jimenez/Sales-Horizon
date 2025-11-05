# === Chromebook Sales Forecasting Dashboard ===
# Run this file with: streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly

st.set_page_config(page_title="Chromebook Sales Forecasting", layout="wide")
st.title("💻 Chromebook Sales Forecasting Dashboard")

# Sidebar upload
st.sidebar.header("Upload or Use Sample Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.sidebar.info("No file uploaded — using sample data.")
    dates = pd.date_range(start="2022-01-01", periods=36, freq="M")
    sales = [1500 + i*30 + (i%5)*100 for i in range(len(dates))]
    df = pd.DataFrame({"Date": dates, "Sales": sales})

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

st.write("### 📈 Historical Sales Data", df.tail())
fig = px.line(df, x="Date", y="Sales", title="Historical Chromebook Sales", markers=True)
st.plotly_chart(fig, use_container_width=True)

periods = st.sidebar.slider("Forecast Months", 3, 24, 12)
train = df.rename(columns={"Date": "ds", "Sales": "y"})
model = Prophet()
model.fit(train)
future = model.make_future_dataframe(periods=periods, freq="M")
forecast = model.predict(future)

st.subheader("🔮 Forecasted Sales")
fig2 = plot_plotly(model, forecast)
st.plotly_chart(fig2, use_container_width=True)

csv = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].rename(columns={
    "ds": "Date", "yhat": "Predicted", "yhat_lower": "Lower", "yhat_upper": "Upper"
})
st.download_button("📥 Download Forecast CSV", data=csv.to_csv(index=False).encode("utf-8"), file_name="forecast.csv")

st.success("✅ Dashboard ready! Run locally on Chromebook Linux via Streamlit.")

