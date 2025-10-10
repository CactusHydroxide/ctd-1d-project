import streamlit as st

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

# cart state

if 'cart_items' not in st.session_state:
    # temporary for testing
    st.session_state['cart_items'] = {'Apple': 3,'Orange': 2}
    # st.session_state['cart_items'] = {}


# init page
pg = st.navigation(pages)
pg.run()

# Website init page. Write your page code in the individual pages.