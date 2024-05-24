import sys
from PyQt5.QtWidgets import QApplication
from window import Window
from buttons import Buttons
from style import Styles


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.buttons = Buttons()

        self.window.layout.addLayout(self.buttons.layout)
        Styles.apply_style(self.window)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = App()
    app.run()