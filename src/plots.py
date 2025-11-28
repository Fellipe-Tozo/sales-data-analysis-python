import matplotlib.pyplot as plt




def plot_sales_by_month(sales_by_month, out_path='outputs/sales_by_month.png'):
plt.figure(figsize=(8,4))
plt.plot(sales_by_month['order_month'].astype(str), sales_by_month['line_total'])
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(out_path)
plt.close()




def plot_top_products(top_products, out_path='outputs/top_products.png', top_n=10):
top = top_products.head(top_n)
plt.figure(figsize=(8,4))
plt.bar(top['product_name'], top['revenue'])
plt.xticks(rotation=45, ha='right')
plt.title('Top Products by Revenue')
plt.tight_layout()
plt.savefig(out_path)
plt.close()
