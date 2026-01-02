from prophet import Prophet
import pandas as pd

def generate_forecast(df):
    df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]], model
