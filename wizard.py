from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel, QLineEdit,
                               QMessageBox, QRadioButton, QVBoxLayout, QWizard,
                               QWizardPage)

from enum import IntEnum
from pathlib import Path
import sys
import os

# Special pages starts at 100
# wrapper = 100
# uninstall = 101


class Pages(IntEnum):
    page_start = 0
    page_install = 1
    page_clone = 2
    page_wrapper = 3
    page_uninstall = 4


# Need to prevent crashes due to PyInstaller
def get_localdir():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))

    if getattr(sys, 'frozen', False):
        return base_path
    else:
        return os.path.dirname(os.path.abspath(__file__))


class pageStart(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Leshade")

        self.top_label = QLabel(
            "This wizard will help you register your copy of "
            "<i>Super Product One</i>&trade; or start "
            "evaluating the product"
        )
        self.top_label.setWordWrap(True)

        self.register_radio_button = QRadioButton("&Register your copy")
        self.register_radio_button.setChecked(True)

        self.evaluate_radio_button = QRadioButton(
            "&Evaluate the product for 30 days")
        layout = QVBoxLayout(self)
        layout.addWidget(self.top_label)
        layout.addWidget(self.register_radio_button)
        layout.addWidget(self.evaluate_radio_button)

    def nextId(self):
        return Pages.page_install


class LeShadeManager(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._pages = [pageStart()]

        for page in self._pages:
            self.addPage(page)

        uninstall_button = self.WizardButton.CustomButton1
        self.setOption(QWizard.WizardOption.HaveCustomButton1, True)

        self.setStartId(Pages.page_start)

        self.setWindowTitle("LeShade")


def main():
    app = QApplication(sys.argv)

    app.setOrganizationName("Ishidawg")
    app.setOrganizationDomain("LeShade")

    local_dir = get_localdir()
    icon_path = os.path.join(local_dir, "assets", "logo.png")

    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    wizard = LeShadeManager()
    wizard.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
