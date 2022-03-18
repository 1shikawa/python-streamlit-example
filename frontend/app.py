import json

import requests
import streamlit as st

API_URL = 'http://127.0.0.1:3000'

page = st.sidebar.selectbox("Choose your page", ["example"])

if page == "example":
    st.title("example")

    url = f"{API_URL}/hello"
    res = requests.get(url)
    st.write(res.status_code)
    if res.status_code == 200:
        st.success("hello")
    st.json(res.json())
