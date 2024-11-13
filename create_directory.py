import os

# Directory name
directory = "love_gifs"

# Parent Directory path
parent_dir = "."

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{directory}' created successfully")
except OSError as error:
    print(f"Directory '{directory}' can not be created: {error}")