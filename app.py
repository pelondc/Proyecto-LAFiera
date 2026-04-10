def main():
    print("App inicial - estructura lista")

if __name__ == "__main__":
    main()
from models.gbm import simulate_gbm_terminal


def main():
    spot = 100
    drift = 0.08
    volatility = 0.25
    tenor_years = 0.5
    simulations = 10000

    terminal_prices = simulate_gbm_terminal(
        spot=spot,
        drift=drift,
        volatility=volatility,
        tenor_years=tenor_years,
        simulations=simulations
    )

    print("Número de simulaciones:", len(terminal_prices))
    print("Precio promedio terminal:", round(terminal_prices.mean(), 2))
    print("Precio mínimo:", round(terminal_prices.min(), 2))
    print("Precio máximo:", round(terminal_prices.max(), 2))


if __name__ == "__main__":
    main()
