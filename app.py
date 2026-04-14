from models.pricing import black_scholes_call, black_scholes_put


def main():
    S = 100   # spot
    K = 100   # strike
    T = 0.5   # 6 meses
    r = 0.1083
    sigma = 0.25

    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)

    print("Call price:", round(call, 2))
    print("Put price:", round(put, 2))


if __name__ == "__main__":
    main()
