# Avg_Trend_Microservice
This project implements a microservice that calculates the average and determines the trend (increasing, decreasing, or constant) of a list of numbers. The communication between the client and server is handled using ZeroMQ.

## Requirements
- Python
-`numpy` library
- `zmq` library

Install the required libraries using pip:
pip install numpy pyzmq

### Requesting Data

To request data from the microservice, run the avg_trend_service.py first and send a list of numbers as a space-separated string to the server using the `calculate_average_and_trend` method in the `Avg_trend_client` class. The server will process the data and return the average and trend.
