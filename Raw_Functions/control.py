import socket


class Control:
    def __init__(self, ip_address, port=23):
        self.ip = ip_address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip_address, port))

def pwon(self):
    command = "PWR ON\r"
    self.s.sendall(command.encode())

def pwoff(self):
    command = "PWR OFF\r"
    self.s.sendall(command.encode())
