from numpy import log, sqrt, exp
from scipy.stats import norm as N
   
def blackScholes(time_to_maturity:float, current_price:float, strike_price:float, interest_rate:float, volatility:float):
    S_t = current_price
    r = interest_rate
    K = strike_price
    sigma = volatility
    t = time_to_maturity

    # Intermediate Step
    d1 = ( log(S_t/K) + (r + 0.5 * sigma**2)*t ) / ( sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)

    # Calculate Call and Put Price
    C = N.cdf(d1)*S_t - N.cdf(d2)*K*exp(-r*t)
    P = K * exp(-r*t) * N.cdf(-d2) - current_price * N.cdf(-d1)

    return C, P


if __name__ == "__main__":
    C, P = blackScholes(current_price=100, strike_price=100, time_to_maturity=1, volatility=0.2, interest_rate=0.05)
    print(C, P)
    