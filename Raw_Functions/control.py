import socket


class Control:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def pw_on(self):
        command = "POWR 1\r"
        self.s.sendall(command.encode())

    def pw_off(self):
        command = "POWR 0\r"
        self.s.sendall(command.encode())

    def connect(self, ip, port=4352):
        self.s.connect((ip, port))

    @staticmethod
    def discover():
        broadcast_address = "<broadcast>"
        port = 4352

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.settimeout(2)

        ips = []
        names = []

        try:
            s.sendto("PJLINK 1\r\n".encode(), (broadcast_address, port))
            while True:
                data, address = s.recvfrom(1024)
                if data:
                    ips.append(address[0])
        except socket.timeout:
            pass

        try:
            s.sendto("NAME ?\r\n".encode(), (broadcast_address, port))
            while True:
                data, address = s.recvfrom(1024)
                if data:
                    projector_name = data.decode().strip()
                    names.append(projector_name)
        except socket.timeout:
            pass
        finally:
            s.close()

        return ips, names
