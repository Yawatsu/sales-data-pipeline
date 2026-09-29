USE SalesDataPipeline;
GO

-- ============================================
-- 1. KPIs PRINCIPALES
-- ============================================

SELECT
    SUM(Revenue) AS TotalRevenue,
    COUNT(*) AS TotalOrders,
    AVG(Revenue) AS AverageOrderValue,
    COUNT(DISTINCT CustomerID) AS TotalCustomers
FROM dbo.Sales;


-- ============================================
-- 2. PORCENTAJE DE PEDIDOS RETRASADOS
-- ============================================

SELECT
    COUNT(*) AS TotalOrders,
    SUM(CASE WHEN Delayed = 1 THEN 1 ELSE 0 END) AS DelayedOrders,
    CAST(
        100.0 * SUM(CASE WHEN Delayed = 1 THEN 1 ELSE 0 END)
        / COUNT(*)
        AS DECIMAL(5,2)
    ) AS DelayedOrderPercentage
FROM dbo.Sales;


-- ============================================
-- 3. VENTAS ONLINE VS IN-STORE
-- ============================================

SELECT
    Channel,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    CAST(
        100.0 * SUM(Revenue)
        / (SELECT SUM(Revenue) FROM dbo.Sales)
        AS DECIMAL(5,2)
    ) AS RevenuePercentage
FROM dbo.Sales
GROUP BY Channel
ORDER BY TotalRevenue DESC;


-- ============================================
-- 4. INGRESOS POR REGIÓN
-- ============================================

SELECT
    Region,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    AVG(Revenue) AS AverageOrderValue
FROM dbo.Sales
GROUP BY Region
ORDER BY TotalRevenue DESC;


-- ============================================
-- 5. INGRESOS POR CATEGORÍA
-- ============================================

SELECT
    Category,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    CAST(
        100.0 * SUM(Revenue)
        / (SELECT SUM(Revenue) FROM dbo.Sales)
        AS DECIMAL(5,2)
    ) AS RevenuePercentage
FROM dbo.Sales
GROUP BY Category
ORDER BY TotalRevenue DESC;


-- ============================================
-- 6. INGRESOS MENSUALES
-- ============================================

SELECT
    Month,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    AVG(Revenue) AS AverageOrderValue
FROM dbo.Sales
GROUP BY Month
ORDER BY Month;


-- ============================================
-- 7. RIESGO DE CHURN
-- ============================================

SELECT
    ChurnRisk,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    CAST(
        100.0 * COUNT(*)
        / (SELECT COUNT(*) FROM dbo.Sales)
        AS DECIMAL(5,2)
    ) AS OrderPercentage
FROM dbo.Sales
GROUP BY ChurnRisk
ORDER BY
    CASE ChurnRisk
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
    END;


-- ============================================
-- 8. TIEMPO DE ENTREGA
-- ============================================

SELECT
    Delayed,
    COUNT(*) AS Orders,
    AVG(DeliveryDays) AS AverageDeliveryDays,
    MIN(DeliveryDays) AS MinimumDeliveryDays,
    MAX(DeliveryDays) AS MaximumDeliveryDays
FROM dbo.Sales
GROUP BY Delayed
ORDER BY Delayed;