import streamlit as st
import mylibrary
import datetime

st.title("Sales")
sales_data = mylibrary.get_sales()
sku = mylibrary.get_sku()

# Format Transaction Data
item_qty = {}
category_qty = {}
total_revenue = 0

# sum item and product qty
for transaction in sales_data:
    total_revenue += transaction['price']
    # count items and qty
    for [product,qty] in transaction['items'].items():
        # item += 
        if product in item_qty:
            item_qty[product] += qty
        else:
            item_qty[product] = qty

        # category += 
        cat = sku[product]['category'].capitalize()
        if cat in category_qty:
            category_qty[cat] += qty
        else:
            category_qty[cat] = qty


# Total Revenue, Average Transaction, Latest Transaction Price
st.subheader('Revenue')
revenue_columns = st.columns(3)
revenue_columns[0].metric(label='Total Revenue', value=f'${total_revenue:.2f}')
revenue_columns[1].metric(label='Average Transaction Value', value=f'${total_revenue/len(sales_data):.2f}')
revenue_columns[2].metric(label='Latest Transaction', value=f'${sales_data[-1]['price']:.2f}')

'---'
# Item and Category Sales (tabbed)
st.subheader('Item Sales')
(product_tab, category_tab) =st.tabs(['By Product','By Category'])
with product_tab:
    st.bar_chart(item_qty, horizontal=True)
with category_tab:
    st.bar_chart(category_qty, horizontal=True)

'---'
# Transaction History
st.header('Transaction History')
with st.container(height=700):
    for idx, transactions in enumerate(sales_data[::-1]):
        # transaction id & timestamp
        st.html(f'<h3 style="margin-bottom:0">Transaction ID: 100000{len(sales_data)-idx}</h3>')
        st.html(f'<h3 style="margin-top:0">{transactions['timestamp'].strftime("%d %b %Y %H:%M:%S")}</h3>')
        (item_name_col, item_total_price_col, item_qty_col) = st.columns(3, vertical_alignment='center',)

        # items bought
        item_name_col.html(f'<h4>Item</h4>')
        item_total_price_col.html(f'<h4>Price</h4>')
        item_qty_col.html(f'<h4>Quantity</h4>')

        for product,qty in transactions['items'].items():
            with item_name_col:
                st.write(product)
            with item_total_price_col:
                st.write(f'${qty*sku[product]['price']:.2f}')
            with item_qty_col:
                st.write(str(qty))

        st.html('<h3 style="margin:0">Total Price</h3>')
        st.html(f'<h3 style="margin:0">${transactions['price']}</h3>')
        '---'

