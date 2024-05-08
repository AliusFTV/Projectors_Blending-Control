from PyQt5.QtWidgets import QPushButton, QLabel, QTextEdit, QWidget, QVBoxLayout
from Raw_Functions import control


class Buttons(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Статус:")
        self.layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.button_pwon = QPushButton("Включить проекторы")
        self.layout.addWidget(self.button_pwon)

        self.button_pwoff = QPushButton("Выключить проекторы")
        self.layout.addWidget(self.button_pwoff)

        self.button_discover = QPushButton("Найти проекторы")
        self.layout.addWidget(self.button_discover)

    def pwon(self):
        control.pwon(self.projectors)
        self.text_edit.append("Проектор(ы) включены.")

    def pwoff(self):
        control.pwoff(self.projectors)
        self.text_edit.append("Проектор(ы) выключены.")

    def discover(self):
        self.projectors = control.discover()
        self.text_edit.clear()
        self.text_edit.append("Найденные проекторы:")
        for idx, projector_ip in enumerate(self.projectors):
            self.text_edit.append(f"{idx + 1}. {projector_ip}")
