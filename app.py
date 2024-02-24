
# Project: Price elasticity
# Authors: 
# - Luis Armando Quintanilla Villon
# - Danny Perilla Mikan


import streamlit as st


def config_init():
    """ 
    Initial setup
    """
    # Configure the page to use a broader layout
    st.set_page_config(layout="wide")
    st.title("Price Elasticity Application")
    st.markdown(f'<div style="margin-top: 120px;"></div>', unsafe_allow_html=True)


def input():
    """
    Reults from input
    """
    # Sidebar
    resultado = None
    with st.sidebar:
        st.header("What are the product to research? \n Write their ID:")
        product1 = st.text_input("Product 1")
        product2 = st.text_input("Product 2")
        product3 = st.text_input("Product 3")
    return resultado

    
def main() -> None:
    config_init()


if __name__ == '__main__':
    main()
    