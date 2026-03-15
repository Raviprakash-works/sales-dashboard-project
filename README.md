Here's the raw README content — select all and copy:

📊 Sales Performance Analytics Dashboard

End-to-end sales analytics project — Python EDA, SQL analysis, and a 3-page interactive Power BI dashboard built on the Sample Superstore dataset to uncover regional performance, discount impact, and profitability drivers.


🔍 Problem Statement
Sales teams often lack visibility into which products, regions, and customer segments are actually profitable — and which are quietly destroying margins through excessive discounting. This project analyzes 5,009 orders across 4 years to surface the key drivers of sales performance and build an executive-ready dashboard that enables data-backed decisions.

📁 Project Structure
sales-dashboard-project/
│
├── data/
│   └── Sample - Superstore.csv
│
├── outputs/
│   ├── charts/                        # 9 EDA charts (PNG)
│   └── data/                          # SQL-ready summary tables
│       ├── superstore_cleaned.csv
│       ├── summary_by_category.csv
│       ├── summary_by_region.csv
│       ├── summary_by_subcategory.csv
│       ├── summary_by_segment.csv
│       └── summary_by_year.csv
│
├── screenshots/
│   ├── sales-page1.png
│   ├── sales-page2.png
│   └── sales-page3.png
│
├── superstore_analysis.py
├── superstore_queries.sql
├── Sales_Performance_Dashboard_RaviPrakash.pbix
└── README.md

🛠️ Tools & Technologies
ToolPurposePython (Pandas, Matplotlib, Seaborn)Data cleaning, feature engineering, EDASQL (SQLite)Aggregation queries, cross-dimensional analysisPower BIInteractive 3-page executive dashboardExcelRaw data source

📊 Dashboard Pages
Page 1 — Executive Overview
Show Image

Total Sales, Profit, Orders & Margin % KPI cards
Sales & Profit by Category
Sales & Profit by Region
Yearly Sales & Profit Growth

Page 2 — Deep Dive
Show Image

Sub-Category Profitability line chart with zero reference line
Total Profit by Discount Band
Sales by Segment
Sales & Profit by Ship Mode

Page 3 — Trends & Insights
Show Image

Monthly Sales Trend (2014–2017)
Sales by Quarter & Year
Top 10 Customers by Sales
Region × Category Performance Matrix
Slicers: Order Year, Region


🔑 Key Findings
#FindingInsight1Total revenue $2,297,201 across 4 years12.5% overall profit margin2Technology top category at $836,154Highest margin category3West region leads with $725,458 in salesMost profitable region4Tables losing -$17,725Pricing/discount problem5High discounts (40%+) losing -$99,559Discounting destroys margins6No discount orders generate $329,988 profit3× more than discounted orders7Consumer segment = 50.56% of salesCore revenue driver8Q4 consistently strongest every yearSeasonal pattern for planning9Central region Furniture loss-making (-$2,871)Regional pricing issue10Sales growing year-over-year 2014–2017Positive business trajectory

⚙️ How to Run
Python EDA
bashpip install pandas matplotlib seaborn numpy
python superstore_analysis.py
```

### SQL Queries
```
Import superstore_cleaned.csv into DB Browser for SQLite
Run superstore_queries.sql
```

### Power BI Dashboard
```
1. Open Sales_Performance_Dashboard_RaviPrakash.pbix
2. Update data source path to your local outputs/data/ folder
3. Refresh data
4. Use slicers on Page 3 to filter by Year and Region

📂 Dataset

Source: Sample Superstore Dataset via Kaggle
Records: 9,994 rows · 5,009 unique orders
Features: 21 columns
Period: January 2014 – December 2017


👤 Author
Ravi Prakash

📧 prakash.ravi.works@gmail.com
💼 linkedin.com/in/ravi-prakash-works
🐙 github.com/raviprakash-works
🌐 raviprakash-works.github.io



Project 2 of my data analytics portfolio. Built to demonstrate end-to-end BI skills — from raw Excel through Python EDA and SQL to an executive-level Power BI dashboard.
