from avg_trend_client import *

if __name__ == "__main__":
    client = Avg_trend_client()

    numbers = [10, 20, 30, 40, 50]
    print("Sending numbers:", numbers)
    response = client.calculate_average_and_trend(numbers)
    print("Received response:", response)

    numbers = []
    print("\nSending numbers:", numbers)
    response = client.calculate_average_and_trend(numbers)
    print("Received response:", response)

    numbers = [50, 40, 30, 20, 10]
    print("\nSending numbers:", numbers)
    response = client.calculate_average_and_trend(numbers)
    print("Received response:", response)

    numbers = [10, 11, 12, 10, 13, 14, 15]
    print("\nSending numbers:", numbers)
    response = client.calculate_average_and_trend(numbers)
    print("Received response:", response)