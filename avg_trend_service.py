import zmq

import numpy as np

def determine_trend(numbers):
    x = np.arange(len(numbers))
    y = np.array(numbers)

    m, b = np.polyfit(x, y, 1)

    if m > 0:
        return "increasing"
    elif m < 0:
        return "decreasing"
    else:
        return "constant"


def calculate_average(numbers):
    if not numbers:
        return "Error: No numbers provided"
    numbers = [float(num) for num in numbers]
    average = sum(numbers) / len(numbers)
    trend = determine_trend(numbers)
    return f"Average: {average}, Trend: {trend}"

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_string()
        numbers = message.split()
        result = calculate_average(numbers)
        socket.send_string(result)

if __name__ == "__main__":
    main()