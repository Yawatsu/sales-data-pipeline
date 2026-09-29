USE SalesDataPipeline;
GO

-- ============================================
-- 1. INGRESOS TOTALES
-- ============================================

SELECT
    SUM(Revenue) AS TotalRevenue
FROM dbo.Sales;


-- ============================================
-- 2. TOTAL DE PEDIDOS
-- ============================================

SELECT
    COUNT(*) AS TotalOrders
FROM dbo.Sales;


-- ============================================
-- 3. INGRESOS POR REGIÓN
-- ============================================

SELECT
    Region,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    AVG(Revenue) AS AverageRevenue
FROM dbo.Sales
GROUP BY Region
ORDER BY TotalRevenue DESC;


-- ============================================
-- 4. INGRESOS POR CATEGORÍA
-- ============================================

SELECT
    Category,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue
FROM dbo.Sales
GROUP BY Category
ORDER BY TotalRevenue DESC;


-- ============================================
-- 5. INGRESOS POR CANAL
-- ============================================

SELECT
    Channel,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue,
    AVG(Revenue) AS AverageOrderValue
FROM dbo.Sales
GROUP BY Channel
ORDER BY TotalRevenue DESC;


-- ============================================
-- 6. INGRESOS MENSUALES
-- ============================================

SELECT
    Month,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue
FROM dbo.Sales
GROUP BY Month
ORDER BY Month;


-- ============================================
-- 7. PEDIDOS RETRASADOS
-- ============================================

SELECT
    Delayed,
    COUNT(*) AS Orders,
    AVG(DeliveryDays) AS AverageDeliveryDays
FROM dbo.Sales
GROUP BY Delayed;


-- ============================================
-- 8. RIESGO DE CHURN
-- ============================================

SELECT
    ChurnRisk,
    COUNT(*) AS Orders,
    SUM(Revenue) AS TotalRevenue
FROM dbo.Sales
GROUP BY ChurnRisk
ORDER BY TotalRevenue DESC;