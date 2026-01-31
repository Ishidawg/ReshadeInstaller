import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget,
)

from widgets.widget_title import WidgetTitle
from widgets.pages.page_start import PageStart
from widgets.widget_bottom_buttons import WidgetBottomButtons


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        WINDOW_SIZE = [600, 500]

        self.setWindowTitle("LeShade")
        self.setMinimumSize(WINDOW_SIZE[0], WINDOW_SIZE[1])

        # main widget (page)
        widget_main = QWidget()
        self.setCentralWidget(widget_main)

        # main layout (inside main widget)
        self.layout_main = QVBoxLayout(widget_main)

        # Instance other pages
        self.page_start = PageStart()

        # Connect signals (if there is signals)
        self.page_start.install.connect(self.on_install_clicked)
        self.page_start.uninstall.connect(self.on_uninstall_clicked)

        # add widgets
        self.layout_main.addWidget(WidgetTitle())
        self.layout_main.addWidget(self.page_start, 1)
        # self.layout_main.addWidget(WidgetBottomButtons())

    # Signals connections
    @Slot(bool)
    def on_install_clicked(self, value):
        print(f"Clicked {value}")

    @Slot(bool)
    def on_uninstall_clicked(self, value):
        print(f"Clicked {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setOrganizationName("Ishidawg")
    app.setApplicationName("LeShade")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
