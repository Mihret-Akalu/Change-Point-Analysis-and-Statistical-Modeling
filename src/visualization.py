import matplotlib.pyplot as plt
import arviz as az

def plot_raw_prices(df):
    plt.figure(figsize=(14,6))
    plt.plot(df["Date"], df["Price"], color="steelblue")
    plt.title("Brent Prices (1987–2022)")
    plt.xlabel("Date")
    plt.ylabel("USD per Barrel")
    plt.grid(alpha=0.3)
    plt.show()

def plot_log_returns(df):
    plt.figure(figsize=(14,6))
    plt.plot(df["Date"], df["log_return"], color="darkorange")
    plt.title("Log Returns")
    plt.grid(alpha=0.3)
    plt.show()

def plot_trace_and_posterior(trace):
    az.plot_trace(trace)
    plt.show()
    az.plot_posterior(trace)
    plt.show()
