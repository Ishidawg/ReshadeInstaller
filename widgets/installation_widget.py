import sys

from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QHBoxLayout,
  QWidget,
  QLineEdit,
  QRadioButton
)

from PySide6.QtCore import Qt

# l:    label
# c:    container
# ly:   layout
# b:    button
# r:    radio

class InstallationWidget(QWidget):

  def __init__(self):
    super().__init__()

    # Create layout and containers
    ly = QVBoxLayout()
    ly.setAlignment(Qt.AlignTop | Qt.AlignmentFlag.AlignLeft)

    c_browse = QWidget()
    c_browse.setContentsMargins(0, 0, 0, 40)
    ly_browse = QHBoxLayout(c_browse)

    c_api = QWidget()
    ly_api = QHBoxLayout(c_api)

    # Widgets
    l_exe = QLabel("Select games executable")
    l_exe.setContentsMargins(10, 0, 0, 0)
    l_exe.setWordWrap(True)
    l_exe.setAlignment(Qt.AlignmentFlag.AlignLeft)
    l_exe.setStyleSheet("font-size: 12pt; font-weight: 100;")

    self.line_edit = QLineEdit()
    self.browse_button = QPushButton("Browse")

    l_api = QLabel("Select games API")
    l_api.setContentsMargins(10, 0, 0, 0)
    l_api.setWordWrap(True)
    l_api.setAlignment(Qt.AlignmentFlag.AlignLeft)
    l_api.setStyleSheet("font-size: 12pt; font-weight: 100;")

    self.r_vulkan = QRadioButton("Vulkan")
    self.r_d3d9 = QRadioButton("DirectX 9")
    self.r_d3d10 = QRadioButton("DirectX 10")
    self.r_vulkan.setChecked(True)

    # Add widgets
    ly.addWidget(l_exe)
    ly.addWidget(c_browse)
    ly.addWidget(l_api)
    ly.addWidget(c_api)

    ly_browse.addWidget(self.line_edit)
    ly_browse.addWidget(self.browse_button)

    for api in (self.r_vulkan, self.r_d3d9, self.r_d3d10):
      ly_api.addWidget(api)

    self.setLayout(ly)





