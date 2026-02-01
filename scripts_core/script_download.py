import re
from PySide6.QtCore import (
    QObject,
    Signal,
    QStandardPaths,
    Slot
)

import urllib.request
import ssl
import certifi

from widgets.pages.page_download import PageDownload

# URL examples
# https://reshade.me/downloads/ReShade_Setup_6.7.1.exe
# https://reshade.me/downloads/ReShade_Setup_6.7.1_Addon.exe

PATTERN = "ReShade_Setup*.exe"


class DownloadWorker(QObject):
    def __init__(self):
        super().__init__()

        self.page_download = PageDownload()

        self.reshade_url = ""
        self.version = ""
        self.release = ""

        self.page_download.version.connect(self.get_version)
        self.page_download.release.connect(self.get_release)

        try:
            self.get_version()
            self.get_release()

            if self.version == "addon":
                self.reshade_url = f"https://reshade.me/downloads/ReShade_Setup_{self.release}_Addon.exe"
            else:
                self.reshade_url = f"https://reshade.me/downloads/ReShade_Setup_{self.release}.exe"
        except Exception as e:
            print(e)

    @Slot(str)
    def get_version(self, value):
        self.version = value

    @Slot(str)
    def get_release(self, value):
        self.release = value
