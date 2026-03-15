"""
=============================================================
Sales Performance Analytics Dashboard
Sample Superstore Dataset — Full EDA & Analysis Pipeline
=============================================================
Author : Ravi Prakash
Dataset: Sample Superstore (Kaggle)
Tools  : Python, Pandas, Matplotlib, Seaborn
Output : Cleaned CSV + charts (PNG) for Power BI & portfolio
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# ── Output folders ─────────────────────────────────────────
os.makedirs('outputs/charts', exist_ok=True)
os.makedirs('outputs/data',   exist_ok=True)

# ── Style ──────────────────────────────────────────────────
ACCENT  = '#c8f53a'
BG      = '#0f0f0f'
SURFACE = '#1a1a1a'
TEXT    = '#edebe4'
MUTED   = '#888880'
PALETTE = ['#c8f53a','#4da6ff','#ff6b6b','#ffd93d','#6bcb77','#ff922b','#c77dff']

plt.rcParams.update({
    'figure.facecolor' : BG,
    'axes.facecolor'   : SURFACE,
    'axes.edgecolor'   : '#2a2a2a',
    'axes.labelcolor'  : MUTED,
    'axes.titlecolor'  : TEXT,
    'xtick.color'      : MUTED,
    'ytick.color'      : MUTED,
    'text.color'       : TEXT,
    'grid.color'       : '#222222',
    'grid.linestyle'   : '--',
    'grid.alpha'       : 0.5,
    'font.family'      : 'monospace',
    'axes.spines.top'  : False,
    'axes.spines.right': False,
})

def save(name):
    path = f'outputs/charts/{name}.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'  ✓ Saved {path}')


# ═══════════════════════════════════════════════════════════
# 1. LOAD & INSPECT
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 1 — Load & Inspect')
print('═'*55)

# Try reading with different encodings
for enc in ['utf-8', 'latin-1', 'cp1252']:
    try:
        df = pd.read_csv('Sample - Superstore.csv', encoding=enc)
        print(f'  Loaded with encoding: {enc}')
        break
    except:
        continue

print(f'  Shape      : {df.shape[0]:,} rows × {df.shape[1]} columns')
print(f'  Columns    : {list(df.columns)}')
print(f'  Nulls      : {df.isnull().sum().sum()}')
print(f'  Duplicates : {df.duplicated().sum()}')


# ═══════════════════════════════════════════════════════════
# 2. CLEAN & ENGINEER FEATURES
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 2 — Clean & Feature Engineering')
print('═'*55)

# Parse dates
df['Order Date']  = pd.to_datetime(df['Order Date'])
df['Ship Date']   = pd.to_datetime(df['Ship Date'])

# Extract time features
df['Order Year']  = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Quarter'] = df['Order Date'].dt.quarter
df['Order YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)
df['Ship Days']   = (df['Ship Date'] - df['Order Date']).dt.days

# Profit Margin %
df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).round(2)

# Sales bands
df['Sales Band'] = pd.cut(
    df['Sales'],
    bins=[0, 100, 500, 1000, 5000, 100000],
    labels=['<$100', '$100–500', '$500–1K', '$1K–5K', '$5K+']
)

# Discount bands
df['Discount Band'] = pd.cut(
    df['Discount'],
    bins=[-0.01, 0, 0.2, 0.4, 0.8],
    labels=['No Discount', 'Low (1–20%)', 'Medium (21–40%)', 'High (41%+)']
)

print(f'  New columns: Order Year, Month, Quarter, YearMonth, Ship Days, Profit Margin %, Sales Band, Discount Band')
print(f'  Final shape: {df.shape}')

df.to_csv('outputs/data/superstore_cleaned.csv', index=False)
print('  ✓ Saved outputs/data/superstore_cleaned.csv')


# ═══════════════════════════════════════════════════════════
# 3. KEY METRICS
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 3 — Key Metrics')
print('═'*55)

total_sales   = df['Sales'].sum()
total_profit  = df['Profit'].sum()
total_orders  = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()
avg_margin    = df['Profit Margin %'].mean()
avg_discount  = df['Discount'].mean() * 100

print(f'  Total Sales     : ${total_sales:,.0f}')
print(f'  Total Profit    : ${total_profit:,.0f}')
print(f'  Total Orders    : {total_orders:,}')
print(f'  Total Customers : {total_customers:,}')
print(f'  Avg Profit Margin: {avg_margin:.1f}%')
print(f'  Avg Discount    : {avg_discount:.1f}%')


# ═══════════════════════════════════════════════════════════
# 4. VISUALISATIONS
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 4 — Generating Charts')
print('═'*55)

# ── Chart 1: Sales & Profit by Category ────────────────────
cat = df.groupby('Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)
fig, ax = plt.subplots(figsize=(8,5))
x = range(len(cat))
w = 0.35
bars1 = ax.bar([i - w/2 for i in x], cat['Sales'],   width=w, color=PALETTE[0], label='Sales')
bars2 = ax.bar([i + w/2 for i in x], cat['Profit'],  width=w, color=PALETTE[1], label='Profit')
ax.set_xticks(x); ax.set_xticklabels(cat.index)
ax.set_title('Sales & Profit by Category', fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.legend()
ax.grid(axis='y')
for bar in bars1: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1000, f'${bar.get_height()/1000:.0f}K', ha='center', fontsize=9, color=TEXT)
for bar in bars2: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1000, f'${bar.get_height()/1000:.0f}K', ha='center', fontsize=9, color=TEXT)
save('01_sales_profit_by_category')

# ── Chart 2: Sales by Region ────────────────────────────────
reg = df.groupby('Region')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)
fig, ax = plt.subplots(figsize=(8,5))
x = range(len(reg))
bars1 = ax.bar([i - w/2 for i in x], reg['Sales'],  width=w, color=PALETTE[0], label='Sales')
bars2 = ax.bar([i + w/2 for i in x], reg['Profit'], width=w, color=PALETTE[2], label='Profit')
ax.set_xticks(x); ax.set_xticklabels(reg.index)
ax.set_title('Sales & Profit by Region', fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.legend(); ax.grid(axis='y')
save('02_sales_profit_by_region')

# ── Chart 3: Monthly Sales Trend ───────────────────────────
monthly = df.groupby('Order YearMonth')['Sales'].sum().reset_index()
monthly = monthly.sort_values('Order YearMonth')
fig, ax = plt.subplots(figsize=(14,5))
ax.plot(monthly['Order YearMonth'], monthly['Sales'], color=ACCENT, linewidth=2, marker='o', markersize=3)
ax.fill_between(monthly['Order YearMonth'], monthly['Sales'], alpha=0.15, color=ACCENT)
ax.set_title('Monthly Sales Trend', fontsize=13, fontweight='bold')
ax.set_ylabel('Sales ($)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.set_xticks(ax.get_xticks()[::6])
plt.xticks(rotation=45, ha='right')
ax.grid(axis='y')
save('03_monthly_sales_trend')

# ── Chart 4: Top 10 Sub-Categories by Sales ────────────────
subcat = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=True).tail(10)
fig, ax = plt.subplots(figsize=(9,6))
bars = ax.barh(subcat.index, subcat['Sales'], color=[PALETTE[2] if p < 0 else PALETTE[0] for p in subcat['Profit']], height=0.6)
ax.set_title('Top 10 Sub-Categories by Sales\n(Red = Loss-making)', fontsize=13, fontweight='bold')
ax.set_xlabel('Sales ($)')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.grid(axis='x')
for bar, val in zip(bars, subcat['Sales']): ax.text(val+500, bar.get_y()+bar.get_height()/2, f'${val/1000:.0f}K', va='center', fontsize=9, color=TEXT)
save('04_top_subcategories')

# ── Chart 5: Profit Margin by Category & Segment ───────────
pivot = df.groupby(['Category','Segment'])['Profit Margin %'].mean().unstack()
fig, ax = plt.subplots(figsize=(9,5))
pivot.plot(kind='bar', ax=ax, color=PALETTE[:3], width=0.6)
ax.set_title('Avg Profit Margin % by Category & Segment', fontsize=13, fontweight='bold')
ax.set_ylabel('Profit Margin %')
ax.set_xlabel('')
plt.xticks(rotation=0)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f%%'))
ax.legend(title='Segment')
ax.grid(axis='y')
save('05_profit_margin_category_segment')

# ── Chart 6: Discount vs Profit Scatter ────────────────────
fig, ax = plt.subplots(figsize=(9,6))
scatter = ax.scatter(df['Discount'], df['Profit'],
                     c=df['Sales'], cmap='RdYlGn',
                     alpha=0.4, s=20)
plt.colorbar(scatter, ax=ax, label='Sales ($)')
ax.axhline(0, color=PALETTE[2], linestyle='--', linewidth=1.5, alpha=0.7)
ax.set_title('Discount vs Profit (colored by Sales)', fontsize=13, fontweight='bold')
ax.set_xlabel('Discount Rate')
ax.set_ylabel('Profit ($)')
ax.xaxis.set_major_formatter(mticker.PercentFormatter(1.0))
ax.grid(True)
save('06_discount_vs_profit')

# ── Chart 7: Sales by Segment ───────────────────────────────
seg = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6,6))
wedges, texts, autotexts = ax.pie(seg.values, labels=seg.index,
                                   colors=PALETTE[:3], autopct='%1.1f%%',
                                   startangle=90, wedgeprops=dict(width=0.55))
ax.set_title('Sales Distribution by Segment', fontsize=13, fontweight='bold')
for at in autotexts: at.set_fontsize(11)
save('07_sales_by_segment')

# ── Chart 8: Yearly Sales & Profit Growth ──────────────────
yearly = df.groupby('Order Year')[['Sales','Profit']].sum()
fig, ax = plt.subplots(figsize=(8,5))
x = yearly.index
ax.bar([i - w/2 for i in x], yearly['Sales'],  width=w, color=PALETTE[0], label='Sales')
ax.bar([i + w/2 for i in x], yearly['Profit'], width=w, color=PALETTE[1], label='Profit')
ax.set_title('Yearly Sales & Profit Growth', fontsize=13, fontweight='bold')
ax.set_xlabel('Year'); ax.set_xticks(x)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.legend(); ax.grid(axis='y')
save('08_yearly_growth')

# ── Chart 9: Ship Mode Analysis ─────────────────────────────
ship = df.groupby('Ship Mode')[['Sales','Profit']].sum().sort_values('Sales', ascending=True)
fig, ax = plt.subplots(figsize=(8,5))
x = range(len(ship))
ax.barh([i - w/2 for i in x], ship['Sales'],  height=w, color=PALETTE[0], label='Sales')
ax.barh([i + w/2 for i in x], ship['Profit'], height=w, color=PALETTE[1], label='Profit')
ax.set_yticks(x); ax.set_yticklabels(ship.index)
ax.set_title('Sales & Profit by Ship Mode', fontsize=13, fontweight='bold')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'${x/1000:.0f}K'))
ax.legend(); ax.grid(axis='x')
save('09_ship_mode_analysis')


# ═══════════════════════════════════════════════════════════
# 5. SQL-READY SUMMARY TABLES
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 5 — Export Summary Tables')
print('═'*55)

# By Category
cat_summary = df.groupby('Category').agg(
    TotalSales    = ('Sales',   'sum'),
    TotalProfit   = ('Profit',  'sum'),
    TotalOrders   = ('Order ID','nunique'),
    AvgDiscount   = ('Discount', lambda x: round(x.mean()*100,1)),
    AvgMargin     = ('Profit Margin %', lambda x: round(x.mean(),1))
).reset_index()
cat_summary['TotalSales']  = cat_summary['TotalSales'].round(0)
cat_summary['TotalProfit'] = cat_summary['TotalProfit'].round(0)
cat_summary.to_csv('outputs/data/summary_by_category.csv', index=False)
print('  ✓ summary_by_category.csv')

# By Region
reg_summary = df.groupby('Region').agg(
    TotalSales    = ('Sales',   'sum'),
    TotalProfit   = ('Profit',  'sum'),
    TotalOrders   = ('Order ID','nunique'),
    AvgMargin     = ('Profit Margin %', lambda x: round(x.mean(),1))
).reset_index().sort_values('TotalSales', ascending=False)
reg_summary['TotalSales']  = reg_summary['TotalSales'].round(0)
reg_summary['TotalProfit'] = reg_summary['TotalProfit'].round(0)
reg_summary.to_csv('outputs/data/summary_by_region.csv', index=False)
print('  ✓ summary_by_region.csv')

# By Sub-Category
subcat_summary = df.groupby(['Category','Sub-Category']).agg(
    TotalSales    = ('Sales',   'sum'),
    TotalProfit   = ('Profit',  'sum'),
    AvgDiscount   = ('Discount', lambda x: round(x.mean()*100,1)),
    AvgMargin     = ('Profit Margin %', lambda x: round(x.mean(),1))
).reset_index().sort_values('TotalSales', ascending=False)
subcat_summary.to_csv('outputs/data/summary_by_subcategory.csv', index=False)
print('  ✓ summary_by_subcategory.csv')

# By Segment
seg_summary = df.groupby('Segment').agg(
    TotalSales    = ('Sales',   'sum'),
    TotalProfit   = ('Profit',  'sum'),
    TotalCustomers= ('Customer ID','nunique'),
    AvgOrderValue = ('Sales',   'mean'),
    AvgMargin     = ('Profit Margin %', lambda x: round(x.mean(),1))
).reset_index()
seg_summary.to_csv('outputs/data/summary_by_segment.csv', index=False)
print('  ✓ summary_by_segment.csv')

# Yearly summary
yearly_summary = df.groupby('Order Year').agg(
    TotalSales    = ('Sales',   'sum'),
    TotalProfit   = ('Profit',  'sum'),
    TotalOrders   = ('Order ID','nunique'),
    TotalCustomers= ('Customer ID','nunique'),
    AvgMargin     = ('Profit Margin %', lambda x: round(x.mean(),1))
).reset_index()
yearly_summary.to_csv('outputs/data/summary_by_year.csv', index=False)
print('  ✓ summary_by_year.csv')


# ═══════════════════════════════════════════════════════════
# 6. KEY FINDINGS
# ═══════════════════════════════════════════════════════════
print('\n' + '═'*55)
print('  STEP 6 — Key Findings')
print('═'*55)

top_cat    = cat_summary.sort_values('TotalSales', ascending=False).iloc[0]
top_region = reg_summary.iloc[0]
loss_subcat = df.groupby('Sub-Category')['Profit'].sum().sort_values().iloc[0]
loss_name   = df.groupby('Sub-Category')['Profit'].sum().sort_values().index[0]
high_disc   = df[df['Discount'] >= 0.4]['Profit'].mean()
low_disc    = df[df['Discount'] < 0.2]['Profit'].mean()

print(f"""
  1. Total Sales             : ${total_sales:,.0f}
  2. Total Profit            : ${total_profit:,.0f} (Margin: {total_profit/total_sales*100:.1f}%)
  3. Top category by sales   : {top_cat['Category']} (${top_cat['TotalSales']:,.0f})
  4. Top region by sales     : {top_region['Region']} (${top_region['TotalSales']:,.0f})
  5. Biggest loss sub-cat    : {loss_name} (${loss_subcat:,.0f})
  6. Avg profit (disc ≥40%)  : ${high_disc:,.0f} vs ${low_disc:,.0f} (low discount)
  7. Total unique customers  : {total_customers:,}
  8. Total unique orders     : {total_orders:,}
""")

print('═'*55)
print('  ✅  All done!')
print('  Charts → outputs/charts/')
print('  Data   → outputs/data/')
print('  Load superstore_cleaned.csv into Power BI next.')
print('═'*55 + '\n')
