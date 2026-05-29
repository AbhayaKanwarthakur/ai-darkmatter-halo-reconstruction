import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_curve(df):
    scaler = MinMaxScaler()
    df["velocity_norm"] = scaler.fit_transform(
        df[["velocity"]]
    )
    return df
