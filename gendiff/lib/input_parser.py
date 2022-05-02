import json
import yaml
from pathlib import Path


def open_files(path: str) -> dict:
    """Открытие файлов нужного формата"""
    ext = Path(path).suffix
    if ext == '.json':
        content = json.load(open(path))
        return content
    elif ext == '.yml' or ext == '.yaml':
        content = yaml.load(open(path), Loader=yaml.BaseLoader)
        return content
    else:
        return "Wrong file format"
