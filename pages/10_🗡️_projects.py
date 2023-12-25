import streamlit as st

def bcall():

    st.write('button call')

st.title('hamburger， ye！')

with st.sidebar:
    b1 = st.button('Button', on_click=bcall)
