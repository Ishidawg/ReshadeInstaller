import shutil
import os

from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from PySide6.QtCore import Qt
from scripts_core.script_manager import update_manager, read_manager_content


class PageUninstall(QWidget):

    def __init__(self):
        super().__init__()

        self.games: list[str] = read_manager_content("game")
        self.games_dir: list[str] = read_manager_content("dir")

        # create layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # create widgets
        label_description = QLabel("Select a game and click uninstall")
        label_description.setStyleSheet("font-size: 12pt; font-weight: 100")
        label_description.setWordWrap(True)

        self.game_list = QListWidget(self)
        self.add_items(self.games, self.game_list)

        self.btn_uninstall = QPushButton("Uninstall")
        self.btn_uninstall.clicked.connect(
            lambda: self.uninstall_reshade(self.game_list, self.games_dir))

        # add widgets
        layout.addWidget(label_description)
        layout.addWidget(self.game_list)
        layout.addWidget(self.btn_uninstall)
        self.setLayout(layout)

    def add_items(self, games, widget_list):
        index = 1

        for game in games:
            newItem = QListWidgetItem()
            newItem.setText(game)
            widget_list.insertItem(index, newItem)

            index = index + 1

    def uninstall_reshade(self, widget_list, dir_list):

        try:
            current_row = widget_list.currentRow()
            game_path = dir_list[current_row]

            shaders_dir = os.path.join(game_path, "Shaders")
            textures_dir = os.path.join(game_path, "Textures")

            files_tbr = ["opengl32.dll", "d3d8.dll", "d3d9.dll",
                         "d3d10.dll", "d3d11.dll", "dxgi.dll", "d3dcompiler_47.dll", "ReShade.ini", "ReShade.log", "ReShadePreset.ini"]

            if os.path.exists(shaders_dir) and os.path.exists(textures_dir):
                shutil.rmtree(shaders_dir)
                shutil.rmtree(textures_dir)

            for file in files_tbr:
                if file in os.listdir(game_path):
                    os.remove(os.path.join(game_path, file))

            # Remove game from list
            widget_list.takeItem(current_row)

            update_manager(current_row)

            print(current_row)
            print(game_path)
        except IndexError as e:
            print(e)
