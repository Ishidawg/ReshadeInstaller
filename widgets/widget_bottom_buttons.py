from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QWidget,
    QPushButton
)

from PySide6.QtCore import Qt


class WidgetBottomButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom |
                            Qt.AlignmentFlag.AlignCenter)

        self.bnt_next = QPushButton("Next")
        self.btn_back = QPushButton("Back")

        layout.addWidget(self.bnt_next)
        layout.addWidget(self.btn_back)

        self.setLayout(layout)
