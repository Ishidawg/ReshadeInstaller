from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QWizardPage, QWizard
import sys


def create_start_page():
    page = QWizardPage()
    page.setTitle("Downloading")

    label = QLabel("LeShade is a manager for reshade installations on linux. It's a native tool that can install and uninstall reshade across many games that uses proton or WINE.")
    label.setWordWrap(True)

    layout = QVBoxLayout(page)
    layout.addWidget(label)

    return page


def create_intall_page():
    page = QWizardPage()
    page.setTitle("Installing")

    label = QLabel("FOCK")
    label.setWordWrap(True)

    layout = QVBoxLayout(page)
    layout.addWidget(label)

    return page


def create_uninstall_page():
    page = QWizardPage()
    page.setTitle("Installing")

    label = QLabel("FOCK")
    label.setWordWrap(True)

    layout = QVBoxLayout(page)
    layout.addWidget(label)

    return page


def main():
    QApplication(sys.argv)

    wizard = QWizard()
    wizard.addPage(create_start_page())
    wizard.addPage(create_intall_page())

    def switch_uninstall(page):
        wizard.addPage(page)

    uninstall_button = wizard.WizardButton.CustomButton1
    wizard.setButtonText(uninstall_button, "Uninstall")
    wizard.setOption(wizard.WizardOption.HaveCustomButton1, True)

    wizard.customButtonClicked.connect(
        switch_uninstall(create_uninstall_page()))

    wizard.setWindowTitle("LeShade")
    wizard.show()

    sys.exit(wizard.exec())


if __name__ == '__main__':
    main()
