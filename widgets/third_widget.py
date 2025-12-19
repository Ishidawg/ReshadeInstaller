import sys

from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

from PySide6.QtCore import Qt

# l:    label
# c:    container
# ly:   layout
# b:    button

class ThirdWidget(QWidget):

  def __init__(self):
    super().__init__()

    # Create layout
    ly = QVBoxLayout()
    ly.setAlignment(Qt.AlignCenter | Qt.AlignmentFlag.AlignCenter)

    # Label
    l_description = QLabel("THIRD SCREEN")
    l_description.setStyleSheet("font-size: 22pt;")

    # Add widgets
    ly.addWidget(l_description)
    self.setLayout(ly)





