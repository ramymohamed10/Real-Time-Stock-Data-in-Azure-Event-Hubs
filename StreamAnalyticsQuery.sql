-- Azure Stream Analytics query to transform and load data
SELECT
    -- Convert the 'Stock_Timestamp' field to a DATETIME type and rename it as 'Stock_Timestamp'.
    CAST([Stock_Timestamp] AS DATETIME) AS Stock_Timestamp,

    -- Convert the 'Open_Price' field to a FLOAT type and rename it as 'Open_Price'.
    CAST([Open_Price] AS FLOAT) AS Open_Price,

    -- Convert the 'High_Price' field to a FLOAT type and rename it as 'High_Price'.
    CAST([High_Price] AS FLOAT) AS High_Price,

    -- Convert the 'Low_Price' field to a FLOAT type and rename it as 'Low_Price'.
    CAST([Low_Price] AS FLOAT) AS Low_Price,

    -- Convert the 'Close_Price' field to a FLOAT type and rename it as 'Close_Price'.
    CAST([Close_Price] AS FLOAT) AS Close_Price,

    -- Convert the 'AdjClose_Price' field to a FLOAT type and rename it as 'AdjClose_Price'.
    CAST([AdjClose_Price] AS FLOAT) AS AdjClose_Price,

    -- Convert the 'Volume' field to a BIGINT type and rename it as 'Volume'.
    CAST([Volume] AS BIGINT) AS Volume

-- Specifies the destination for the data (the 'stockdb' table).
INTO
    [stockdb]

-- Specifies the source of the data (the 'msftstock' stream).
FROM
    [msftstock]

-- Filters the data to include only rows where the 'Volume' is greater than 100,000.
WHERE 
    [Volume] > 100000 -- Only select rows where volume is greater than 100,000
