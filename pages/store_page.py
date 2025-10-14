import streamlit as st
import mylibrary
st.title("Store")


#example code for item qty
def add(product_name):
    mylibrary.add_cart_qty(product_name)
def sub(product_name):
    mylibrary.subtract_cart_qty(product_name)
st.write('Store Page')

cart = mylibrary.get_cart()
sku = mylibrary.get_sku()

categories = ['Fruits','Vegetable','Drinks']
columns = st.columns(3) # (col1, col2, col3)


for product_index, product in enumerate(sku.items()): # get product's index in list and product details
    column_index = product_index % 3 # get column number
    with columns[column_index]:
        with st.container():

            # display product details
            quantity = cart.get(product[0], 0)
            st.subheader(product[0])
            st.text(f'${float(product[1]['price']):.2f}')
            st.text(f'Quantity: {quantity}')
            plus_minus_column = st.columns(2)
            # display image

            # display add and subtract buttons
            with plus_minus_column[0]:
                st.button('\-', on_click=sub,args= (product[0],), key=f'{product[0]}_subtract' )
            with plus_minus_column[1]:
                st.button('\+', on_click=add,args= (product[0],), key=f'{product[0]}_add')