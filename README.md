# Avg_Trend_Microservice
This project implements a microservice that calculates the average and determines the trend (increasing, decreasing, or constant) of a list of numbers. The communication between the client and server is handled using ZeroMQ.

## Requirements
- Python
-`numpy` library
- `zmq` library

Install the required libraries using pip:
pip install numpy pyzmq

### Requesting&Reciving Data

To request data from the microservice, run the avg_trend_service.py first and send a list of numbers as a space-separated string to the server using the `calculate_average_and_trend` method in the `Avg_trend_client` class. The server will process the data and return the average and trend.

#### Example Request

```python
from avg_trend_client import Avg_trend_client

client = Avg_trend_client()

# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Send the request to the microservice
response = client.calculate_average_and_trend(numbers)
print("Received response:", response)
