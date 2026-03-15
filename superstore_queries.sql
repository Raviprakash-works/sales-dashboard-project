-- =============================================================
-- Sales Performance Analytics — SQL Queries
-- Author : Ravi Prakash
-- Tool   : SQLite / PostgreSQL / MySQL compatible
-- Note   : Import superstore_cleaned.csv as table 'superstore'
-- =============================================================


-- ─────────────────────────────────────────────────────────────
-- 1. OVERVIEW — Total KPIs
-- ─────────────────────────────────────────────────────────────
SELECT
    COUNT(DISTINCT "Order ID")                          AS TotalOrders,
    COUNT(DISTINCT "Customer ID")                       AS TotalCustomers,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS OverallMarginPct,
    ROUND(AVG(Discount) * 100, 1)                       AS AvgDiscountPct,
    ROUND(AVG(Sales), 2)                                AS AvgOrderValue
FROM superstore;


-- ─────────────────────────────────────────────────────────────
-- 2. SALES & PROFIT BY CATEGORY
-- ─────────────────────────────────────────────────────────────
SELECT
    Category,
    COUNT(DISTINCT "Order ID")                          AS Orders,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct,
    ROUND(AVG(Discount) * 100, 1)                       AS AvgDiscountPct
FROM superstore
GROUP BY Category
ORDER BY TotalSales DESC;


-- ─────────────────────────────────────────────────────────────
-- 3. SALES & PROFIT BY REGION
-- ─────────────────────────────────────────────────────────────
SELECT
    Region,
    COUNT(DISTINCT "Order ID")                          AS Orders,
    COUNT(DISTINCT "Customer ID")                       AS Customers,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY Region
ORDER BY TotalSales DESC;


-- ─────────────────────────────────────────────────────────────
-- 4. SUB-CATEGORY PROFITABILITY (find loss-makers)
-- ─────────────────────────────────────────────────────────────
SELECT
    Category,
    "Sub-Category",
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct,
    ROUND(AVG(Discount) * 100, 1)                       AS AvgDiscountPct,
    CASE WHEN SUM(Profit) < 0 THEN 'Loss-Making' ELSE 'Profitable' END AS Status
FROM superstore
GROUP BY Category, "Sub-Category"
ORDER BY TotalProfit ASC;


-- ─────────────────────────────────────────────────────────────
-- 5. YEARLY SALES & PROFIT GROWTH
-- ─────────────────────────────────────────────────────────────
SELECT
    "Order Year",
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    COUNT(DISTINCT "Order ID")                          AS TotalOrders,
    COUNT(DISTINCT "Customer ID")                       AS TotalCustomers,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY "Order Year"
ORDER BY "Order Year";


-- ─────────────────────────────────────────────────────────────
-- 6. DISCOUNT IMPACT ON PROFIT
-- ─────────────────────────────────────────────────────────────
SELECT
    "Discount Band",
    COUNT(*)                                            AS OrderLines,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(AVG(Profit), 2)                               AS AvgProfitPerLine,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY "Discount Band"
ORDER BY AvgProfitPerLine DESC;


-- ─────────────────────────────────────────────────────────────
-- 7. SALES BY SEGMENT
-- ─────────────────────────────────────────────────────────────
SELECT
    Segment,
    COUNT(DISTINCT "Customer ID")                       AS Customers,
    COUNT(DISTINCT "Order ID")                          AS Orders,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(AVG(Sales), 2)                                AS AvgOrderValue,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY Segment
ORDER BY TotalSales DESC;


-- ─────────────────────────────────────────────────────────────
-- 8. SHIP MODE PERFORMANCE
-- ─────────────────────────────────────────────────────────────
SELECT
    "Ship Mode",
    COUNT(*)                                            AS OrderLines,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(AVG("Ship Days"), 1)                          AS AvgShipDays,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY "Ship Mode"
ORDER BY TotalSales DESC;


-- ─────────────────────────────────────────────────────────────
-- 9. TOP 10 CUSTOMERS BY SALES
-- ─────────────────────────────────────────────────────────────
SELECT
    "Customer Name",
    Segment,
    Region,
    COUNT(DISTINCT "Order ID")                          AS TotalOrders,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY "Customer Name", Segment, Region
ORDER BY TotalSales DESC
LIMIT 10;


-- ─────────────────────────────────────────────────────────────
-- 10. REGION × CATEGORY CROSS ANALYSIS
-- ─────────────────────────────────────────────────────────────
SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 1)           AS MarginPct
FROM superstore
GROUP BY Region, Category
ORDER BY Region, TotalSales DESC;


-- ─────────────────────────────────────────────────────────────
-- 11. LOSS-MAKING ORDERS (deep discount problem)
-- ─────────────────────────────────────────────────────────────
SELECT
    Category,
    "Sub-Category",
    Region,
    Segment,
    ROUND(Sales, 2)                                     AS Sales,
    ROUND(Profit, 2)                                    AS Profit,
    ROUND(Discount * 100, 0)                            AS DiscountPct,
    ROUND("Profit Margin %", 1)                         AS MarginPct
FROM superstore
WHERE Profit < 0
    AND Discount >= 0.4
ORDER BY Profit ASC
LIMIT 20;


-- ─────────────────────────────────────────────────────────────
-- 12. QUARTERLY SALES TREND
-- ─────────────────────────────────────────────────────────────
SELECT
    "Order Year",
    "Order Quarter",
    ROUND(SUM(Sales), 0)                                AS TotalSales,
    ROUND(SUM(Profit), 0)                               AS TotalProfit,
    COUNT(DISTINCT "Order ID")                          AS TotalOrders
FROM superstore
GROUP BY "Order Year", "Order Quarter"
ORDER BY "Order Year", "Order Quarter";
