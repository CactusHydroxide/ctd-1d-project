import streamlit as st
import mylibrary
st.title("Store")


# Add and Sub qty on_click functions
def add(product_name):
    mylibrary.add_cart_qty(product_name)


def sub(product_name):
    mylibrary.subtract_cart_qty(product_name)


cart = mylibrary.get_cart()
sku = mylibrary.get_sku()

categories = ['Fruits', 'Vegetable', 'Drinks']
columns = st.columns(3)  # (col1, col2, col3)

# show individual products
# loop thru sku and get product's index in list and product details
for product_index, product in enumerate(sku.items()):
    column_index = product_index % 3  # get column number
    with columns[column_index]:
        with st.container(border=True):

            # display product details
            st.subheader(product[0])

            # display price
            st.text(f'${float(product[1]['price']):.2f}')

            # display image
            st.image(product[1]['image_url'], use_container_width='always')

            # display add and subtract buttons
            plus_minus_column = st.columns(3, vertical_alignment='center')
            quantity = cart.get(product[0], 0)
            with plus_minus_column[0]:
                st.button(
                    '\-', on_click=sub, args=(product[0],), key=f'{product[0]}_subtract', width='stretch')
            with plus_minus_column[1]:
                st.html(
                    f'<p style="width: auto; height:auto; margin:auto; text-align: center;">{quantity}</p>')
            with plus_minus_column[2]:
                st.button(
                    '\+', on_click=add, args=(product[0],), key=f'{product[0]}_add', width='stretch')
