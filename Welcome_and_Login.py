import streamlit as st
import pandas as pd
import numpy as np
from openpyxl import Workbook, load_workbook
import helper
import datetime as datetime
import time
#from state import provide_state

st.set_page_config(
    page_title="StakeInsights: Intelligent Metrics to Empower Your Business",
    page_icon="stakeinsights logo only.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = 'False'

#st.components.v1.html(custom_html)
st.image('stakeinsights_banner.png')
#st.title('Stake Insights')

st.header('Welcome to Stake Insights.')
st.markdown('**We give you visibility into the metrics you need to run your business.**')
st.divider()

#st.text('Please login below to get started.')



col1, col2 = st.columns(2, gap='large')

with col1:
    placeholder = st.empty()

with col2:
    st.image('lock.jpg')


# Insert a form in the container
with placeholder.form("login", border = False):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
    st.markdown(
    """
    <hr style="margin-top: 20px; margin-bottom: 12px;">
    <p style="text-align: center; color: #808080; font-size: 15px;">
    © | <a href="https://www.bluetide.co/">Bluetide</a> 
    </p>
    """,
    unsafe_allow_html=True,
)

if submit and email == st.secrets['app_username'] and password == st.secrets['app_password']:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.session_state['logged_in'] = 'True'
    st.success("Login successful; choose an action in the sidebar to continue.")
elif submit and email != st.secrets['app_username'] and password != st.secrets['app_password']:
    st.session_state['logged_in'] = 'False'
    #st.error("Login failed! Try again or contact admin for assistance.")
else:
    pass