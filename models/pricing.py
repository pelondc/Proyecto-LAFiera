import numpy as np
from scipy.stats import norm


def black_scholes_call(S, K, T, r, sigma):
    """
    Precio de una opción Call europea (Black-Scholes)
    """

    if S <= 0 or K <= 0:
        raise ValueError("S y K deben ser mayores a 0")
    if T <= 0:
        raise ValueError("T debe ser mayor a 0")
    if sigma <= 0:
        raise ValueError("sigma debe ser mayor a 0")

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(S, K, T, r, sigma):
    """
    Precio de una opción Put europea (Black-Scholes)
    """

    if S <= 0 or K <= 0:
        raise ValueError("S y K deben ser mayores a 0")
    if T <= 0:
        raise ValueError("T debe ser mayor a 0")
    if sigma <= 0:
        raise ValueError("sigma debe ser mayor a 0")

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price
