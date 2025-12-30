from PySide6.QtCore import QObject, Signal
import os
import shutil
import subprocess

REPO_URLS = {
  "default": "https://github.com/crosire/reshade-shaders.git",
  "prod80": "https://github.com/prod80/prod80-ReShade-Repository.git",
  "quint": "https://github.com/martymcmodding/qUINT.git"
}

TEMP_DIR = "./reshade/temp_clones"

class CloneWorker(QObject):
  finished = Signal()
  status_update = Signal(str)
  progress_update = Signal(int)
  error = Signal(str)

  def __init__(self):
    super().__init__()
    self.game_dir = None
    self.selected_repos = []

  def setup(self, game_dir, selections):
    self.game_dir = game_dir
    self.selected_repos = selections

  def run(self):
    try:
      if not self.game_dir or not os.path.isdir(self.game_dir):
        raise ValueError("Invalid game directory.")

      shaders_dest = os.path.join(self.game_dir, "Shaders")
      textures_dest = os.path.join(self.game_dir, "Textures")
      
      os.makedirs(shaders_dest, exist_ok=True)
      os.makedirs(textures_dest, exist_ok=True)

      os.makedirs(TEMP_DIR, exist_ok=True)

      total_repos = len(self.selected_repos)
      current_repo = 0
      self.progress_update.emit(0)

      for repo_key in self.selected_repos:
        url = REPO_URLS.get(repo_key)
        if not url: continue

        repo_name = repo_key
        self.status_update.emit(f"Cloning {repo_name} repository")
        
        temp_repo_path = os.path.join(TEMP_DIR, repo_name)
        
        if os.path.exists(temp_repo_path):
          shutil.rmtree(temp_repo_path)

        try:
          subprocess.run(["git", "clone", url, temp_repo_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
          self.status_update.emit(f"Failed to clone {repo_name}. Skipping.")
          continue

        self.status_update.emit(f"Installing {repo_name} files")
        self._organize_files(temp_repo_path, shaders_dest, textures_dest)

        current_repo += 1
        percentage = int((current_repo / total_repos) * 100)
        self.progress_update.emit(percentage)

      shutil.rmtree(TEMP_DIR, ignore_errors=True)
      
      self.status_update.emit("All shaders installed!")
      self.finished.emit()

    except Exception as e:
      self.error.emit(str(e))

  def _organize_files(self, source_root, shaders_dest, textures_dest):
    for root, dirs, files in os.walk(source_root):
      if ".git" in root: continue

      for file in files:
        file_lower = file.lower()
        src_file = os.path.join(root, file)
        
        if file_lower.endswith(('.fx', '.fxh')):
          shutil.copy2(src_file, os.path.join(shaders_dest, file))
        
        elif file_lower.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tga')):
          shutil.copy2(src_file, os.path.join(textures_dest, file))
          