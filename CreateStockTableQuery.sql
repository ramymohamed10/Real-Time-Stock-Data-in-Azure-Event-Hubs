-- Create a new table named StockData
CREATE TABLE StockData
(
    -- StockDataID column: an integer that auto-increments starting from 1. It is the primary key and cannot be null.
    StockDataID INT IDENTITY(1,1) PRIMARY KEY NOT NULL,

    -- Stock_Timestamp column: stores date and time values.
    Stock_Timestamp DATETIME,

    -- Open_Price column: a floating-point number representing the stock's opening price.
    Open_Price FLOAT,

    -- High_Price column: a floating-point number representing the highest price of the stock.
    High_Price FLOAT,

    -- Low_Price column: a floating-point number representing the lowest price of the stock.
    Low_Price FLOAT,

    -- Close_Price column: a floating-point number representing the stock's closing price.
    Close_Price FLOAT,

    -- AdjClose_Price column: a floating-point number representing the stock's adjusted closing price.
    AdjClose_Price FLOAT,

    -- Volume column: a large integer representing the number of shares traded.
    Volume BIGINT,
)
