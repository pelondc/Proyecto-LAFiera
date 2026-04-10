def simulate_gbm():
    pass
import numpy as np


def simulate_gbm_terminal(
    spot: float,
    drift: float,
    volatility: float,
    tenor_years: float,
    simulations: int,
    random_seed: int | None = 42
) -> np.ndarray:
    """
    Simula precios terminales usando Geometric Brownian Motion (GBM).

    Fórmula:
        ST = S0 * exp((mu - 0.5 * sigma^2) * T + sigma * sqrt(T) * Z)

    Parámetros:
        spot: precio actual del subyacente
        drift: retorno esperado anual
        volatility: volatilidad anual
        tenor_years: tiempo al vencimiento en años
        simulations: número de simulaciones Monte Carlo
        random_seed: semilla para reproducibilidad

    Regresa:
        np.ndarray con los precios terminales simulados
    """

    if spot <= 0:
        raise ValueError("spot must be greater than 0.")
    if volatility < 0:
        raise ValueError("volatility cannot be negative.")
    if tenor_years <= 0:
        raise ValueError("tenor_years must be greater than 0.")
    if simulations <= 0:
        raise ValueError("simulations must be greater than 0.")

    rng = np.random.default_rng(random_seed)
    z = rng.standard_normal(simulations)

    diffusion = volatility * np.sqrt(tenor_years) * z
    drift_term = (drift - 0.5 * volatility**2) * tenor_years

    terminal_prices = spot * np.exp(drift_term + diffusion)
    return terminal_prices


def simulate_gbm_paths(
    spot: float,
    drift: float,
    volatility: float,
    tenor_years: float,
    steps: int,
    simulations: int,
    random_seed: int | None = 42
) -> np.ndarray:
    """
    Simula trayectorias completas de precio usando GBM.

    Regresa:
        np.ndarray de shape (simulations, steps + 1)
    """

    if spot <= 0:
        raise ValueError("spot must be greater than 0.")
    if volatility < 0:
        raise ValueError("volatility cannot be negative.")
    if tenor_years <= 0:
        raise ValueError("tenor_years must be greater than 0.")
    if steps <= 0:
        raise ValueError("steps must be greater than 0.")
    if simulations <= 0:
        raise ValueError("simulations must be greater than 0.")

    rng = np.random.default_rng(random_seed)
    dt = tenor_years / steps

    z = rng.standard_normal((simulations, steps))
    increments = (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z
    log_paths = np.cumsum(increments, axis=1)

    paths = np.zeros((simulations, steps + 1))
    paths[:, 0] = spot
    paths[:, 1:] = spot * np.exp(log_paths)

    return paths
