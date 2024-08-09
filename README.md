# Avg Trend Microservice

This project implements a microservice that calculates the average and determines the trend (increasing, decreasing, or constant) of a list of numbers. The communication between the client and server is handled using ZeroMQ.

## Requirements

- Python 3.x
- `numpy` library
- `zmq` library

## Installation and Usage

### 1. Clone the Repository

First, clone this project from GitHub:

```bash
git clone https://github.com/SimonCX/Avg_Trend_Microservice.git
```
### 2. Enter the Directory
Navigate into the cloned repository's directory:

```bash
cd Avg_Trend_Microservice
```
### 3. Install Dependencies
Install the required Python libraries using pip:

```bash
pip install numpy pyzmq
```
### 4. Run the Service
Start the server by running the following command:

```bash
python avg_trend_server.py
```
