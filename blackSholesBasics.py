from numpy import log, sqrt, exp
from scipy.stats import norm as N

class BlackScholes:
    def __init__(self):
        self.t = None # Time to Maturity
        self.S_t = None # Price of asset
        self.K = None # Strike price
        self.r = None # Interest rate
        self.sigma = None # volatility
        
    def calculate(self, time_to_maturity:float, current_price:float, strike_price:float, interest_rate:float, volatility:float):
        self.S_t = current_price
        self.r = interest_rate
        self.K = strike_price
        self.sigma = volatility
        self.t = time_to_maturity

        # Intermediate Step
        d1 = ( log(self.S_t/self.K) + (self.r + 0.5 * self.sigma**2)*self.t ) / ( self.sigma * sqrt(self.t))
        d2 = d1 - self.sigma * sqrt(self.t)

        # Calculate Call and Put Price
        self.C = N.cdf(d1)*self.S_t - N.cdf(d2)*self.K*exp(-self.r*self.t)
        self.P = self.K * exp(-self.r*self.t) * N.cdf(-d2) - current_price * N.cdf(-d1)
    

if __name__ == "__main__":
    B = BlackScholes()
    B.calculate(current_price=100, strike_price=100, time_to_maturity=1, volatility=0.2, interest_rate=0.05)
    print(B.C)
    print(B.P)