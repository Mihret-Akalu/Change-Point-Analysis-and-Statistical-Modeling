import numpy as np

def add_log_returns(df):
    """
    Adds a log return series for volatility analysis.
    """
    df["log_return"] = np.log(df["Price"]) - np.log(df["Price"].shift(1))
    return df.dropna()
