from typing import Tuple, Union
import numpy as np
from scipy.stats import norm as N
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use("Agg")

   
def blackScholes(S_t:Union[float, np.ndarray], K:float, r:float, sigma:Union[float, np.ndarray], t:float) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Black-Scholes option pricing model for European call and put options.
    Parameters:
        S_t (float or np.ndarray): current_price
        K(float): strike_price
        r(float): interest_rate
        sigma(float or np.ndarray): volatility
        t(float): time_to_maturity
    
    Returns:
        tuple: [float or np.ndarray, float or np.ndarray]: Call and put option price(s)
    """

    # Intermediate Step
    sqrt_t = np.sqrt(t) * sigma
    d1 = ( np.log(S_t / K) + (r + 0.5 * sigma**2) * t ) / sqrt_t
    d2 = d1 - sqrt_t

    # Calculate Call and Put Price
    discounted_k = K * np.exp(-r * t)
    call = N.cdf(d1) * S_t - N.cdf(d2) * discounted_k
    put = discounted_k * N.cdf(-d2) - S_t * N.cdf(-d1)

    return call, put

def plot_heatmap(spot_range, vol_range, strike, time_to_maturity, interest_rate):
    # Vectorized Calculation
    spot_grid, vol_grid = np.meshgrid(spot_range, vol_range)
    s_flat = spot_grid.ravel()
    v_flat = vol_grid.ravel()
    
    call_flat, put_flat = blackScholes(t=time_to_maturity, S_t= s_flat, K=strike, r=interest_rate, sigma= v_flat)
    
    call_prices = call_flat.reshape(vol_grid.shape)
    put_prices = put_flat.reshape(vol_grid.shape)

    # Plotting
    fig_kwargs = dict(figsize=(10, 8), dpi=100)
    x_ticks = np.round(spot_range, 2)
    y_ticks = np.round(vol_range, 2)
    
    fig_call, ax_call = plt.subplots(**fig_kwargs)
    sns.heatmap(call_prices, xticklabels=x_ticks, yticklabels=y_ticks, annot=True, fmt=".2f", cmap="YlOrBr", ax=ax_call, cbar=False)
    ax_call.set_title('CALL')
    ax_call.set_xlabel('Spot Price')
    ax_call.set_ylabel('Volatility')
    
    fig_put, ax_put = plt.subplots(**fig_kwargs)
    sns.heatmap(put_prices, xticklabels=x_ticks, yticklabels=y_ticks, annot=True, fmt=".2f", cmap="YlOrBr", ax=ax_put, cbar=False)
    ax_put.set_title('PUT')
    ax_put.set_xlabel('Spot Price')
    ax_put.set_ylabel('Volatility')


    return fig_call, fig_put



if __name__ == "__main__":
    C, P = blackScholes(S_t=100, K=100, t=1, sigma=0.2, r=0.05)
    print(C, P)
    