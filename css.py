import streamlit as st

# TODO Make own CSS
def css():
    st.markdown("""
<style>
/* Call and Puts */
.metric-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px; /* Adjust the padding to control height */
    width: auto; /* Auto width for responsiveness, or set a fixed width if necessary */
    margin: 0 auto; /* Center the container */
}

.metric-call {
    background-color: #2b8725; /* Green */
    color: black; /* Font Color */
    filter: brightness(2.5);
    border-radius: 10px; /* Rounded corners */
}

.metric-put {
    background-color: #800517; /* Red */
    color: black; /* Font color */
    filter: brightness(2.5);
    border-radius: 10px; /* Rounded corners */
}
                
/* Style for the value text */
.metric-value {
    font-size: 1.5rem; /* Adjust font size */
    font-weight: bold;
    margin: 0; /* Remove default margins */
}

/* Style for the label text */
.metric-label {
    font-size: 1rem; /* Adjust font size */
    margin-bottom: 4px; /* Spacing between label and value */
}


</style>
""", unsafe_allow_html=True)