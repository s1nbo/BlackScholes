import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from blackScholesBasics import blackScholes
from stockdata import stockdata
from css import css

linkedin_url = 'https://www.linkedin.com/in/sinbo/'

css()

with st.sidebar:
    st.title('Black-Scholes Option Model')
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">Sinan Bove</a>', unsafe_allow_html=True)

    current_price = st.number_input("Current Asset Price", value=100.0, step=1.0, min_value=0.01)
    strike = st.number_input("Strike Price", value=100.0, step= 1.0, min_value=0.01)
    time_to_maturity = st.number_input("Time to Maturity (Years)", value=1.0, step=1.0, min_value=0.01)
    volatility = st.number_input("Volatility (σ)", value=0.2, min_value=0.0)
    interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)

    C, P = blackScholes(current_price=current_price, strike_price=strike, time_to_maturity=time_to_maturity, volatility=volatility, interest_rate=interest_rate)
    st.markdown(f'Call Price: {C}')
    st.markdown(f'Put Price: {P}')

col1, col2 = st.columns([1,1], gap="small")

with col1:
    st.markdown(f"""
        <div class="metric-container metric-call">
            <div>
                <div class="metric-label">CALL Value</div>
                <div class="metric-value">${C:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-container metric-put">
            <div>
                <div class="metric-label">PUT Value</div>
                <div class="metric-value">${P:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


data = stockdata()
# Get axis limits
x_min, x_max = data.index.min(), data.index.max()
y_min, y_max = data.min()[0], data.max()[0]

# Create a placeholder
plot_placeholder = st.empty()

# Create figure and axis
fig, ax = plt.subplots()

# Set static axes limits
ax.set_xlim(x_min, x_max)
print(y_min, y_max)
ax.set_ylim(y_min, y_max)

# Animation loop
for i in range(1, len(data) + 1):
    ax.clear()

    # Redraw line with static axis limits
    ax.plot(data.index[:i], data.values[:i], color='blue')
    ax.set_title("AAPL Closing Prices (2020)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.grid(True)
    
    # Static limits
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')


    plot_placeholder.pyplot(fig)
    
    # Wait a short time before showing the next frame