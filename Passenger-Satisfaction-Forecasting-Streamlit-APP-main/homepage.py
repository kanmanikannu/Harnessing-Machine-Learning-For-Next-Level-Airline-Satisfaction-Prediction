import streamlit as st
from function import get_img_as_base64  # Ensure this function exists

# General Page Settings
st.set_page_config(layout="centered", page_title="Airline Prediction",
                   page_icon="")

# Sidebar content
st.sidebar.markdown("<br>", unsafe_allow_html=True)


# Add background and styles
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{img}") no-repeat center top;
            background-size: cover;
        }}
        section[data-testid="stSidebar"] {{
            width: 200px !important;
        }}
    </style>
    """.format(img=get_img_as_base64("./images/Fearless - 7.jpeg")),
    unsafe_allow_html=True,
)

# Title and description
st.markdown(
    """
    <h1 class="title">Welcome to Airline Satisfaction Prediction</h1>
    <p class="me">Your satisfaction is our priority.</p>
    """,
    unsafe_allow_html=True,
)

# Main content image
st.image("./images/Fearless - 3.png")

# Footer
with open("style/footer.html", "r", encoding="utf-8") as pred:
    footer_html = f"""{pred.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)
