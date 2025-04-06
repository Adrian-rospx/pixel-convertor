from pathlib import Path

# source directory path
current_dir = Path(__file__).resolve().parent
# project directory
project_dir = current_dir.parent
# images directory
images_dir = project_dir / "images"

def get_image_path(name: str) -> str:
    img_path = str(images_dir / name)
    return img_path

def suffix(file_path: str) -> str:
    path = Path(file_path)
    return path.suffix

def new_image_path(file_path: str) -> str:
    path = Path(file_path)
    ext = path.suffix

    new = file_path.removesuffix(ext)
    new += "_pixel.png"
    return new