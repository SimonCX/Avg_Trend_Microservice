import zmq

class Avg_trend_client:
    def __init__(self, address="tcp://localhost:5555"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(address)

    def calculate_average_and_trend(self, numbers):
        numbers_str = ' '.join(map(str, numbers))
        self.socket.send_string(numbers_str)
        response = self.socket.recv_string()
        return response
