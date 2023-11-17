# Import necessary libraries
import yfinance as yf
from datetime import datetime, timedelta
import json
import time
from azure.eventhub import EventHubProducerClient, EventData
import os

# Load environment variables from a .env file for security and configuration management
from dotenv import load_dotenv
load_dotenv()

# Retrieve Azure Storage account connection string and Event Hub name from environment variables
connection_str = os.getenv('CONNECTION_STRING')
eventhub_name = os.getenv('EVENTHUB_NAME')

# Initialize an Event Hub producer client to send data to Azure Event Hub
producer = EventHubProducerClient.from_connection_string(
    connection_str, eventhub_name=eventhub_name)

# Define a function to fetch stock data from Yahoo Finance


def get_stock_data(ticker, start_date, end_date):
    # Download stock data for a given ticker, start date, end date, and interval
    data = yf.download(ticker, start=start_date, end=end_date, interval="1m")
    return data


# Calculate the current date and the date 7 days ago
current_date = datetime.now()
date_N_days_ago = current_date - timedelta(days=7)

# Format the dates as strings for use in the yfinance download function
start_date = date_N_days_ago.strftime("%Y-%m-%d")
end_date = current_date.strftime("%Y-%m-%d")

# Fetch stock data for Microsoft (MSFT) for the past 7 days
stock_data = get_stock_data("MSFT", start_date, end_date)

# Save the fetched stock data to a CSV file
stock_data.to_csv('MSFT_stock_data.csv')

# Attempt to send the stock data to Azure Event Hub
try:
    # Open a connection with the producer
    with producer:
        # Iterate over each row in the stock data
        for index, row in stock_data.iterrows():
            # Create a message dictionary with stock data
            message = {
                "Stock_Timestamp": str(index),
                "Open_Price": row["Open"],
                "High_Price": row["High"],
                "Low_Price": row["Low"],
                "Close_Price": row["Close"],
                "AdjClose_Price": row["Adj Close"],
                "Volume": row["Volume"]
            }
            # Send the message as a batch to Azure Event Hub
            producer.send_batch([EventData(json.dumps(message))])
            # Print the sent message for logging
            print(f"Sent data for {index}")
            print(message)
            # Pause for 2 seconds to avoid overwhelming the Event Hub
            time.sleep(2)
# Handle any exceptions that occur during the data sending process
except Exception as e:
    print(f"Error sending data: {e}")
