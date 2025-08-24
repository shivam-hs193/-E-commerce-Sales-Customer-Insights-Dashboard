# src/eda.py
# Usage: python src/eda.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE/'data/processed/ecommerce_orders_clean.csv', parse_dates=['Order_Date'])

# Monthly sales trend
monthly = df.resample('M', on='Order_Date')['Net_Revenue'].sum().reset_index()
plt.figure()
plt.plot(monthly['Order_Date'], monthly['Net_Revenue'])
plt.title('Monthly Net Revenue')
plt.xlabel('Month')
plt.ylabel('Net Revenue')
fig1 = BASE/'reports/figures/monthly_net_revenue.png'
plt.savefig(fig1, bbox_inches='tight')

# Top categories
top_cat = df.groupby('Category')['Net_Revenue'].sum().sort_values(ascending=False).head(10)
plt.figure()
top_cat.plot(kind='bar')
plt.title('Top Categories by Revenue')
plt.xlabel('Category')
plt.ylabel('Net Revenue')
fig2 = BASE/'reports/figures/top_categories.png'
plt.savefig(fig2, bbox_inches='tight')

# Payment mode distribution
pm = df['Payment_Mode'].value_counts()
plt.figure()
pm.plot(kind='bar')
plt.title('Payment Mode Distribution')
plt.xlabel('Payment Mode')
plt.ylabel('Count')
fig3 = BASE/'reports/figures/payment_mode_distribution.png'
plt.savefig(fig3, bbox_inches='tight')

print(f"Saved figures:\n - {fig1}\n - {fig2}\n - {fig3}")
