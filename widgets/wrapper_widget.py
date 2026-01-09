import sys
import os
import struct

from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QVBoxLayout,
  QHBoxLayout,
  QWidget
)

from PySide6.QtCore import Qt

class WrapperWidget(QWidget):

  def __init__(self):
    super().__init__()

    ly = QVBoxLayout()
    ly.setAlignment(Qt.AlignTop | Qt.AlignmentFlag.AlignCenter)

    # Description
    l_description = QLabel("As you are installing reshade on a Direct3D 8.0 game, please add the command bellow to your environment variables or steam launch options.")
    l_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
    l_description.setWordWrap(True)

    # CSS style to command label
    s_code = "background-color: #2b2b2b; color: #ffffff; padding: 5px;"

    # Command widget
    self.l_wrapper_command = QLabel(f"<html>Steam: <span style='{s_code}'>WINEDLLOVERRIDES='d3d8=n,b' %command%</span> <br> Other: <span style='{s_code}'>WINEDLLOVERRIDES='d3d8=n,b</span></html>")
    self.l_wrapper_command.setStyleSheet("font 12pt; font-weight: 600;")
    self.l_wrapper_command.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add widgets
    ly.addWidget(l_description)
    ly.addSpacing(5)
    ly.addWidget(self.l_wrapper_command)

    self.setLayout(ly)
