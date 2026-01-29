import json
import os

from PySide6.QtCore import QStandardPaths

HOME_PATH = QStandardPaths.writableLocation(
    QStandardPaths.StandardLocation.HomeLocation)
LESHADE_PATH = os.path.join(HOME_PATH, ".leshade")

installation_manager = ''

os.makedirs(LESHADE_PATH, exist_ok=True)

try:
    with open(f"{LESHADE_PATH}/manager.json", "x"):
        pass

except Exception as e:
    print(e)

    with open("f{LESHADE_PATH}/manager.json", "r") as json:
        installation_manager.json.loads(f"{LESHADE_PATH}/manager.json")


# installation_manager = open(f"{LESHADE_PATH}/manager.json", "x")
# installation_manager.close()
