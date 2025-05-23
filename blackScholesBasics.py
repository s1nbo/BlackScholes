from numpy import log, sqrt, exp
from scipy.stats import norm as N
from numpy import zeros, round
from matplotlib.pyplot import subplots
from seaborn import heatmap
   
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

def plot_heatmap(spot_range, vol_range, strike, time_to_maturity, interest_rate):
    call_prices = zeros((len(vol_range), len(spot_range)))
    put_prices = zeros((len(vol_range), len(spot_range)))
    
    for i, vol in enumerate(vol_range):
        for j, spot in enumerate(spot_range):
            C, P = blackScholes(time_to_maturity=time_to_maturity, current_price=spot, strike_price=strike, interest_rate=interest_rate, volatility=vol)

            call_prices[i, j] = C
            put_prices[i, j] = P
    
    fig_call, ax_call = subplots(figsize=(10, 8))
    heatmap(call_prices, xticklabels=round(spot_range, 2), yticklabels=round(vol_range, 2), annot=True, fmt=".2f", cmap="YlOrBr", ax=ax_call)
    ax_call.set_title('CALL')
    ax_call.set_xlabel('Spot Price')
    ax_call.set_ylabel('Volatility')
    
    fig_put, ax_put = subplots(figsize=(10, 8))
    heatmap(put_prices, xticklabels=round(spot_range, 2), yticklabels=round(vol_range, 2), annot=True, fmt=".2f", cmap="YlOrBr", ax=ax_put)
    ax_put.set_title('PUT')
    ax_put.set_xlabel('Spot Price')
    ax_put.set_ylabel('Volatility')

    return fig_call, fig_put

    



if __name__ == "__main__":
    C, P = blackScholes(current_price=100, strike_price=100, time_to_maturity=1, volatility=0.2, interest_rate=0.05)
    print(C, P)
    