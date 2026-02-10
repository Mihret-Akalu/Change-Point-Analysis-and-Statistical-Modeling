import pandas as pd

def load_brent_data(path):
    """
    Load Brent price CSV with date conversion and basic validation.
    Returns a cleaned DataFrame.

    Raises:
        FileNotFoundError: If path is invalid
        ValueError: If required columns missing
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {path}")

    if "Date" not in df.columns or "Price" not in df.columns:
        raise ValueError("Required columns 'Date' and 'Price' missing")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Price"])
    df = df.sort_values("Date").reset_index(drop=True)

    return df
