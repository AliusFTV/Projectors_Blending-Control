from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QTextEdit
from Raw_Functions.capture import Capture
from Raw_Functions.render import ImageProcessor


class Buttons(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.btn_check = QPushButton("Check HDMI Connection")
        self.btn_start = QPushButton("Start Video Processing")

        self.layout.addWidget(self.btn_check)
        self.layout.addWidget(self.btn_start)

        self.btn_check.clicked.connect(self.check)
        self.btn_start.clicked.connect(self.start)

    def check(self):
        capture_instance = Capture()
        status = capture_instance.check_hdmi()
        if status:
            self.text_edit.append("HDMI Connection: Connected")
        else:
            self.text_edit.append("HDMI Connection: Not Connected")

    def start(self):
        capture_instance = Capture()
        self.text_edit.append("Starting video processing...")
        processed_video = capture_instance.start_video()
        adjusted_video = ImageProcessor.adjust_brightness(processed_video)
        sharpened_video = ImageProcessor.enhance_sharpness(adjusted_video)
        high_res_video = ImageProcessor.increase_resolution(sharpened_video)
        self.text_edit.append("Video processing complete")