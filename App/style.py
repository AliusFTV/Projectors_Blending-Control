
class Styles:
    @staticmethod
    def apply_style(window):
        window.setStyleSheet("""
            QLabel {
                font-size: 16px;
                margin-bottom: 10px;
            }
            QTextEdit {
                font-size: 14px;
                border: 1px solid black;
                margin-bottom: 10px;
            }
            QPushButton {
                font-size: 16px;
                height: 40px;
            }
        """)

    @staticmethod
    def set_text(text_edit, text):
        text_edit.setPlainText(text)
