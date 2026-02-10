import pymc as pm
import numpy as np

def build_bcp_model(prices):
    """
    Returns a PyMC change point model for a simple 1-point
    Bayesian change point detection.
    """
    n = len(prices)
    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)
        mu1 = pm.Normal("mu1", mu=np.mean(prices), sigma=15)
        mu2 = pm.Normal("mu2", mu=np.mean(prices), sigma=15)
        sigma = pm.HalfNormal("sigma", sigma=10)
        idx = np.arange(n)
        mu = pm.math.switch(idx < tau, mu1, mu2)
        pm.Normal("obs", mu=mu, sigma=sigma, observed=prices)

    return model
