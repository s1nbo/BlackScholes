import streamlit as st
from blackScholesBasics import blackScholes
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


