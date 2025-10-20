import streamlit as st
import datetime

# Navbar
pages = {
    "Home": [
        st.Page("./pages/store_page.py", title="Store"),
        st.Page("./pages/checkout_page.py", title="Checkout"),
    ],
    "Admin": [
        st.Page("./pages/sales_page.py", title="Sales Dashboard"),
    ],
}

# init cart_items state
if 'cart_items' not in st.session_state:
    st.session_state['cart_items'] = {}
    # st.session_state['cart_items'] = {}

# init transaction_history state 
if 'transaction_history' not in st.session_state:
    st.session_state['transaction_history'] = [
        {
            'timestamp': datetime.datetime(2025, 10, 14, 21, 43, 15, 237895),
            'items':  {
                'Apple': 4,
                'Orange': 3,
                'Milk': 2,
                'Kale': 2
            },
            'price': 33.6
        }
    ]

st.session_state['transaction_index'] = 0


# init page
pg = st.navigation(pages)
pg.run()

# Website init page. Write your page code in the individual pages.