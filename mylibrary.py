import json
import streamlit as st

# state and variable management
def get_sku():
    with open('./sku.json', 'r') as sku:
        sku_data = json.load(sku)
    return sku_data

def get_cart():
    if 'cart_items' in st.session_state:
        return(st.session_state['cart_items'])
    else:
        st.warning('Cart Item State is not initialized', icon="⚠️")
def add_cart_qty(cart_item):
    if 'cart_items' in st.session_state:
        if cart_item in st.session_state['cart_items']:
            st.session_state['cart_items'][cart_item] += 1 
        else:
            st.session_state['cart_items'][cart_item] = 0
def subtract_cart_qty(cart_item):
    if 'cart_items' in st.session_state:
        if cart_item in st.session_state['cart_items']:
            st.session_state['cart_items'][cart_item] -= 1 
        else:
            st.session_state['cart_items'][cart_item] = 0


# Cart Logic
def calculate_total( oranges, apples):
    return 2*oranges + 3*apples

def plastic_bags_price(bags):
    """one bag 0.1, two bags 0.4, three bags 0.9 """
    return 0.1*bags*bags
