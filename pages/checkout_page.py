import streamlit as st
import mylibrary
CHECKOUT_LAYOUT = (2,2,1)

st.title('Checkout')
cart_items = list(st.session_state['cart_items'].items())
 
header1, header2, header3 = st.columns(CHECKOUT_LAYOUT, vertical_alignment='center',)
header1.subheader("Item",divider='grey')
header2.subheader("Price",divider='grey')
header3.subheader("Quantity",divider='grey')

#cart item
sku_data = mylibrary.get_sku()
total_price = 0
for item_name, qty in cart_items:
    item_price = f'${sku_data[item_name]['price']:.2f}'
    with st.container():
        item_name_col, item_total_price_col, item_qty_col = st.columns(CHECKOUT_LAYOUT, vertical_alignment='center',)
        with item_name_col:
            st.write(item_name)
        with item_total_price_col:
            st.write(item_price)
        with item_qty_col:
            col1,col2,col3 = st.columns(3,vertical_alignment ='center',gap='small')
            col1.button('\-', key=f'{item_name}_minus', on_click=mylibrary.subtract_cart_qty, args=(item_name,))
            col2.write(str(qty))
            col3.button('\+', key=f'{item_name}_plus', on_click=mylibrary.add_cart_qty, args=(item_name,))    
    total_price += sku_data[item_name]['price'] * qty

# total price
with st.container(horizontal_alignment='right'):
    st.html('<h1 style="text-align:right; margin-bottom:0;">Total Price</h1>')
    st.html(f'<h1 style="text-align:right; margin-top:0">${total_price:.2f}<h1>')

# submit button container
@st.dialog('Clear Cart')
def clear_cart_button():
    st.write('Are you sure you want to empty your cart?')
    with st.container(horizontal_alignment='right',horizontal = True):
        if st.button("Cancel", type='primary'):
            st.rerun()
        if st.button("Clear Cart",type='secondary'):
            mylibrary.clear_cart()
            st.rerun()

with st.container(horizontal_alignment='right',horizontal=True):
    if st.button('Clear cart',type='secondary'):
        clear_cart_button()
    st.button('Checkout', type='primary')
