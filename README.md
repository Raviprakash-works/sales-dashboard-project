📊 Sales Performance Analytics Dashboard

End-to-end sales analytics project — Python EDA, SQL analysis, and a 3-page interactive Power BI dashboard built on the Sample Superstore dataset to uncover regional performance, discount impact, and profitability drivers.


🔍 Problem Statement
Sales teams often lack visibility into which products, regions, and customer segments are actually profitable — and which are quietly destroying margins through excessive discounting. This project analyzes 5,009 orders across 4 years to surface the key drivers of sales performance and build an executive-ready dashboard that enables data-backed decisions.

📁 Project Structure
sales-dashboard-project/
│
├── data/
│   └── Sample - Superstore.csv                        # Raw dataset
│
├── outputs/
│   ├── charts/                                        # 9 EDA charts (PNG)
│   └── data/                                          # SQL-ready summary tables
│       ├── superstore_cleaned.csv                     # Cleaned & feature-engineered
│       ├── summary_by_category.csv
│       ├── summary_by_region.csv
│       ├── summary_by_subcategory.csv
│       ├── summary_by_segment.csv
│       └── summary_by_year.csv
│
├── screenshots/
│   ├── sales-page1.png                                # Overview page
│   ├── sales-page2.png                                # Deep Dive page
│   └── sales-page3.png                                # Trends & Insights page
│
├── superstore_analysis.py                             # Python EDA script
├── superstore_queries.sql                             # 12 SQL analysis queries
├── Sales_Performance_Dashboard_RaviPrakash.pbix       # Power BI dashboard
└── README.md

🛠️ Tools & Technologies
ToolPurposePython (Pandas, Matplotlib, Seaborn)Data cleaning, feature engineering, EDASQL (SQLite)Aggregation queries, cross-dimensional analysisPower BIInteractive 3-page executive dashboardExcelRaw data source

📊 Dashboard Pages
Page 1 — Executive Overview
Show Image

Total Sales, Profit, Orders & Margin % KPI cards
Sales & Profit by Category (clustered bar)
Sales & Profit by Region (clustered column)
Yearly Sales & Profit Growth (line + column combo)

Page 2 — Deep Dive
Show Image

Sub-Category Profitability line chart with zero reference line
Total Profit by Discount Band (manual color-coded bar)
Sales by Segment (donut chart)
Sales & Profit by Ship Mode (clustered bar)

Page 3 — Trends & Insights
Show Image

Monthly Sales Trend with average reference line (2014–2017)
Sales by Quarter & Year (grouped column)
Top 10 Customers by Sales (table with margin %)
Region × Category Performance Matrix
Slicers: Order Year, Region


🔑 Key Findings
#FindingInsight1Total revenue of $2,297,201 across 4 years12.5% overall profit margin2Technology is top category at $836,154 salesHighest margin category3West region leads with $725,458 in salesMost profitable region4Tables sub-category losing -$17,725Pricing/discount problem5High discounts (40%+) average -$99,559 lossDiscounting destroys margins6No discount orders generate $3,29,988 profit3× more than low-discount orders7Consumer segment = 50.56% of total salesCore revenue driver8Q4 consistently strongest quarter every yearSeasonal pattern for planning9Central region Furniture is loss-making (-$2,871)Regional pricing issue10Sales growing year-over-year from 2014–2017Positive business trajectory

⚙️ How to Run
Python EDA
bash# Install dependencies
pip install pandas matplotlib seaborn numpy

# Run analysis
python superstore_analysis.py
Output: 9 charts in outputs/charts/ + cleaned CSV + 5 summary tables in outputs/data/
SQL Queries
bash# Import superstore_cleaned.csv into DB Browser for SQLite
# Run superstore_queries.sql
# 12 queries covering KPIs, category, region, discount impact, top customers
Power BI Dashboard
1. Open Sales_Performance_Dashboard_RaviPrakash.pbix in Power BI Desktop
2. If prompted, update data source path to your local outputs/data/ folder
3. Refresh data
4. Use slicers on Page 3 to filter by Year and Region

📂 Dataset

Source: Sample Superstore Dataset via Kaggle
Records: 9,994 rows · 5,009 unique orders
Features: 21 columns — order details, customer info, product hierarchy, sales, profit, discount, shipping
Time Period: January 2014 – December 2017


🔍 SQL Highlights
12 queries covering:

Overview KPIs (sales, profit, margin, orders)
Category & sub-category profitability
Regional performance breakdown
Discount band impact analysis
Segment & ship mode performance
Top 10 customers by revenue
Quarterly trend analysis
Loss-making orders identification (Query 11)


👤 Author
Ravi Prakash

📧 prakash.ravi.works@gmail.com
💼 LinkedIn
🐙 GitHub
🌐 Portfolio

