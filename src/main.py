import os
from src.etl import load_csvs, transform_merge, compute_kpis
from src.plots import plot_sales_by_month, plot_top_products




def main():
os.makedirs('outputs', exist_ok=True)
customers, orders, items, products = load_csvs('data/customers.csv','data/orders.csv','data/items.csv','data/products.csv')
df = transform_merge(orders, items, products, customers)
kpis = compute_kpis(df)
# salvar outputs
kpis['top_products'].to_csv('outputs/top_products.csv', index=False)
kpis['sales_by_month'].to_csv('outputs/sales_by_month.csv', index=False)
# ajus
