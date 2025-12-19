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

class StartWidget(QWidget):

  def __init__(self):
    super().__init__()

    # Create layout
    ly = QVBoxLayout()
    ly.setAlignment(Qt.AlignCenter | Qt.AlignmentFlag.AlignCenter)

    # Label
    l_description = QLabel("This is a unofficial reshade installer for linux, intented to be used with proton applications, but it may also work with wine games.")
    l_description.setWordWrap(True)
    l_description.setAlignment(Qt.AlignmentFlag.AlignCenter)
    l_description.setStyleSheet("font-size: 12pt; font-weight: 100;")

    # Add widgets
    ly.addWidget(l_description)
    self.setLayout(ly)





