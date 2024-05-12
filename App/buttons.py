from PyQt5.QtWidgets import QPushButton, QLabel, QTextEdit, QWidget, QVBoxLayout
from Raw_Functions.control import Control


class Buttons(QWidget):
    def __init__(self):
        super().__init__()
        self.Control = Control()
        self.ip = []

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Статус:")
        self.layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.button_pwon = QPushButton("Включить проекторы")
        self.button_pwon.clicked.connect(self.pwon)
        self.layout.addWidget(self.button_pwon)

        self.button_pwoff = QPushButton("Выключить проекторы")
        self.button_pwoff.clicked.connect(self.pwoff)
        self.layout.addWidget(self.button_pwoff)

        self.button_discover = QPushButton("Найти проекторы")
        self.button_discover.clicked.connect(self.discover)
        self.layout.addWidget(self.button_discover)

        self.button_connect = QPushButton("Подключиться")
        self.button_connect.clicked.connect(self.connect)
        self.layout.addWidget(self.button_connect)

    def pwon(self):
        self.Control.pw_on()
        self.text_edit.append("Проектор(ы) включены.")

    def pwoff(self):
        self.Control.pw_off()
        self.text_edit.append("Проектор(ы) выключены.")

    def discover(self):
        ips, names = self.Control.discover()
        self.ip.append(ips)
        self.text_edit.clear()
        self.text_edit.append("Найденные проекторы:")
        for idx, (Ip, Name) in enumerate(zip(ips, names)):
            self.text_edit.append(f"{idx + 1}. {Ip} ({Name})")

    def connect(self, ip):
        self.Control.connect(ip)
        self.text_edit.clear()
        self.text_edit.append("Подключено")

