# 📊 Sales Performance Analytics Dashboard

> End-to-end sales analytics project — Python EDA, SQL analysis, and a 3-page interactive Power BI dashboard built on the Sample Superstore dataset to uncover regional performance, discount impact, and profitability drivers.

---

## 🔍 Problem Statement

Sales teams often lack visibility into **which products, regions, and customer segments are actually profitable** — and which are quietly destroying margins through excessive discounting. This project analyzes 5,009 orders across 4 years to surface the key drivers of sales performance and build an executive-ready dashboard that enables data-backed decisions.

---

## 📁 Project Structure

```
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
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** (Pandas, Matplotlib, Seaborn) | Data cleaning, feature engineering, EDA |
| **SQL** (SQLite) | Aggregation queries, cross-dimensional analysis |
| **Power BI** | Interactive 3-page executive dashboard |
| **Excel** | Raw data source |

---

## 📊 Dashboard Pages

### Page 1 — Executive Overview
![Overview](screenshots/sales-page1.png)
- Total Sales, Profit, Orders & Margin % KPI cards
- Sales & Profit by Category (clustered bar)
- Sales & Profit by Region (clustered column)
- Yearly Sales & Profit Growth (line + column combo)

### Page 2 — Deep Dive
![Deep Dive](screenshots/sales-page2.png)
- Sub-Category Profitability line chart with zero reference line
- Total Profit by Discount Band (manual color-coded bar)
- Sales by Segment (donut chart)
- Sales & Profit by Ship Mode (clustered bar)

### Page 3 — Trends & Insights
![Trends](screenshots/sales-page3.png)
- Monthly Sales Trend with average reference line (2014–2017)
- Sales by Quarter & Year (grouped column)
- Top 10 Customers by Sales (table with margin %)
- Region × Category Performance Matrix
- Slicers: Order Year, Region

---

## 🔑 Key Findings

| # | Finding | Insight |
|---|---------|---------|
| 1 | Total revenue of **$2,297,201** across 4 years | 12.5% overall profit margin |
| 2 | **Technology** is top category at $836,154 sales | Highest margin category |
| 3 | **West region** leads with $725,458 in sales | Most profitable region |
| 4 | **Tables sub-category** losing **-$17,725** | Pricing/discount problem |
| 5 | High discounts (40%+) average **-$99,559 loss** | Discounting destroys margins |
| 6 | **No discount orders** generate **$3,29,988 profit** | 3× more than low-discount orders |
| 7 | **Consumer segment** = 50.56% of total sales | Core revenue driver |
| 8 | **Q4 consistently strongest** quarter every year | Seasonal pattern for planning |
| 9 | **Central region Furniture** is loss-making (-$2,871) | Regional pricing issue |
| 10 | Sales growing **year-over-year** from 2014–2017 | Positive business trajectory |

---

## ⚙️ How to Run

### Python EDA
```bash
# Install dependencies
pip install pandas matplotlib seaborn numpy

# Run analysis
python superstore_analysis.py
```
Output: 9 charts in `outputs/charts/` + cleaned CSV + 5 summary tables in `outputs/data/`

### SQL Queries
```bash
# Import superstore_cleaned.csv into DB Browser for SQLite
# Run superstore_queries.sql
# 12 queries covering KPIs, category, region, discount impact, top customers
```

### Power BI Dashboard
```
1. Open Sales_Performance_Dashboard_RaviPrakash.pbix in Power BI Desktop
2. If prompted, update data source path to your local outputs/data/ folder
3. Refresh data
4. Use slicers on Page 3 to filter by Year and Region
```

---

## 📂 Dataset

- **Source:** [Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) via Kaggle
- **Records:** 9,994 rows · 5,009 unique orders
- **Features:** 21 columns — order details, customer info, product hierarchy, sales, profit, discount, shipping
- **Time Period:** January 2014 – December 2017

---

## 🔍 SQL Highlights

12 queries covering:
- Overview KPIs (sales, profit, margin, orders)
- Category & sub-category profitability
- Regional performance breakdown
- Discount band impact analysis
- Segment & ship mode performance
- Top 10 customers by revenue
- Quarterly trend analysis
- Loss-making orders identification (Query 11)

---

## 👤 Author

**Ravi Prakash**
- 📧 prakash.ravi.works@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/ravi-prakash-works)
- 🐙 [GitHub](https://github.com/raviprakash-works)
- 🌐 [Portfolio](https://raviprakash-works.github.io)

---

> *This is Project 2 of my data analytics portfolio. Built to demonstrate end-to-end BI skills — from raw Excel data through Python EDA and SQL analysis to an executive-level Power BI dashboard.*
