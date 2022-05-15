import json
import yaml
from pathlib import Path


def get_data(source, type_data='file'):
    """Получение данных разных типов."""
    if type_data == 'file':
        return _open_files(source)
    else:
        return "Data type not supported"


def _open_files(path: str) -> dict:
    """Открытие файлов нужного формата"""
    ext = Path(path).suffix
    if ext == '.json':
        with open(path) as file:
            content = json.load(file)
        return content
    elif ext == '.yml' or ext == '.yaml':
        with open(path) as file:
            content = yaml.load(file, Loader=yaml.BaseLoader)
        return content
    else:
        return "Wrong file format"
