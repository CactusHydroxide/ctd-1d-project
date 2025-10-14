import json
import streamlit as st

# state and variable management
def get_sku():
    with open('./sku.json', 'r') as sku:
        sku_data = json.load(sku)
    return sku_data


# cart data management
def get_cart():
    if 'cart_items' in st.session_state:
        return(st.session_state['cart_items'])
    else:
        st.warning('Cart Item State is not initialized', icon="⚠️")
def add_cart_qty(cart_item):
    if 'cart_items' in st.session_state:
        if cart_item in st.session_state['cart_items']:
            st.session_state['cart_items'][cart_item] += 1 # change this 
        else:
            st.session_state['cart_items'][cart_item] = 1
def subtract_cart_qty(cart_item):
    if 'cart_items' in st.session_state:
        if cart_item in st.session_state['cart_items'] and st.session_state['cart_items'][cart_item] > 0:
            st.session_state['cart_items'][cart_item] -= 1 # change this
        else:
            st.session_state['cart_items'][cart_item] = 0
def clear_cart():
    st.session_state['cart_items'] = {}

# sales data management
def get_sales():
    return 

def new_sale():
    return