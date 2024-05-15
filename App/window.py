from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from buttons import Buttons
import cv2


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Processing")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.buttons = Buttons()
        self.add_buttons_to_layout()

    def add_buttons_to_layout(self):
        for button in self.buttons.findChildren(QPushButton):
            self.layout.addWidget(button)


