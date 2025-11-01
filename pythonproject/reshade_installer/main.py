from pathlib import Path
from zipfile import ZipFile

def find_reshade(start_path, exe_pattern):
  # start = Path('/home')
  # pattern = 'ReShade_Setup*.exe'
  start = Path(start_path)
  pattern = f'{exe_pattern}'
  matches = list(start.rglob(pattern))

  if not matches:
      return "Reshade was not found"
  return str(matches[0])

def unzip_reshade(source):
  with ZipFile(source, 'r') as zip_object:
    zip_object.extractall("./reshade")

def user_input():

  while True:
    game_bits = int((input("Your game is 32bit or 64bit? [1] - [2]: ")))

    if game_bits <= 2:
      break

  if game_bits == 1:
    find_reshade('./reshade', 'ReShade32.dll')
  else:
    find_reshade('./reshade', 'ReShade64.dll')

def copy_to_folder():
  pass


print("Path:", find_reshade('/home', 'ReShade_Setup*.exe'))
unzip_reshade(find_reshade('/home', 'ReShade_Setup*.exe'))
user_input()