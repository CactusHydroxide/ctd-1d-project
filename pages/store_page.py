import streamlit as st
import mylibrary
st.title("Store")


#example code for item qty
def add():
    mylibrary.add_cart_qty('Apple')
def sub():
    mylibrary.subtract_cart_qty('Apple')
st.write('Store Page')
st.button('Apple +1', on_click=add)
st.button('Apple -1', on_click=sub)


'''
What do to:\n
Make tabs for different sku products. (Fruits, Vegetable, Drinks, Others)\n
Write a loop that iterates over all items in the sku.\n
Each item should show the name, price, and quantity in the cart\n
Use the mylibrary.add_cart_qty and subtract_cart_qty to manage the value'''


'Example of cart data'
st.write(mylibrary.get_cart())

'Example of sku data'
sku_data = mylibrary.get_sku()
sku_data
# your code here