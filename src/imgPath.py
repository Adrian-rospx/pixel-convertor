from pathlib import Path

# source directory path
current_dir = Path(__file__).resolve().parent
# project directory
project_dir = current_dir.parent
# images directory
images_dir = project_dir / "images"

def get_image_path(name: str):
    return images_dir / name
