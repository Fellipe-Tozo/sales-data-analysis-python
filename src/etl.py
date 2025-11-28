import pandas as pd




def load_csvs(path_customers, path_orders, path_items, path_products):
customers = pd.read_csv(path_customers, parse_dates=['created_at'], dayfirst=False)
orders = pd.read_csv(path_orders, parse_dates=['order_date'])
items = pd.read_csv(path_items)
products = pd.read_csv(path_products)
return customers, orders, items, products




def transform_merge(orders, items, products, customers):
# junta order_items com orders e produtos
df = items.merge(orders, on='order_id', how='left') \
.merge(products, on='product_id', how='left') \
.merge(customers, on='customer_id', how='left', suffixes=('', '_cust'))
# calcula total por item e por pedido
df['line_total'] = df['quantity'] * df['unit_price']
# garante tipos
if 'order_date' in df.columns:
df['order_date'] = pd.to_datetime(df['order_date'])
return df




def compute_kpis(df):
total_sales = df['line_total'].sum()
ticket = df.groupby('order_id')['line_total'].sum().mean()
top_products = (df.groupby('product_id')
.agg(product_name=('name','first'),
revenue=('line_total','sum'),
qty=('quantity','sum'))
.sort_values('revenue', ascending=False)
.reset_index())
df['order_month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
sales_by_month = df.groupby('order_month')['line_total'].sum().reset_index()
return {
'total_sales': total_sales,
'ticket_avg': ticket,
'top_products': top_products,
'sales_by_month': sales_by_month
}
