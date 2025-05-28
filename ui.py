import streamlit as st
from blackScholesBasics import blackScholes, plot_heatmap
from css import css
from numpy import linspace

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

    call, put = blackScholes( S_t = current_price, 
        K = strike, 
        t = time_to_maturity, 
        sigma = volatility, 
        r = interest_rate
    )

col1, col2 = st.columns([1,1], gap="small")

with col1:
    st.markdown(f"""
        <div class="metric-container metric-call">
            <div>
                <div class="metric-label">CALL Value</div>
                <div class="metric-value">${call:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-container metric-put">
            <div>
                <div class="metric-label">PUT Value</div>
                <div class="metric-value">${put:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.title("Options Price - Interactive Heatmap")
col1, col2 = st.columns([1,1], gap="small")

spot_range = linspace(current_price - 20, current_price + 20, 10)
vol_range = linspace(volatility - 0.1, volatility + 0.1, 10)

heatmap_fig_call, heatmap_fig_put = plot_heatmap(
    strike=strike, 
    time_to_maturity=time_to_maturity, 
    interest_rate=interest_rate, 
    spot_range=spot_range, 
    vol_range=vol_range
)

with col1:
    st.subheader("Call Price Heatmap")
    st.pyplot(heatmap_fig_call)

with col2:
    st.subheader("Put Price Heatmap")
    st.pyplot(heatmap_fig_put)