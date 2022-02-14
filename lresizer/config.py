import pathlib


BASE_DIR = pathlib.Path(__file__).parent.parent


class ProjectsPaths:
    data_dir = BASE_DIR.joinpath('data')
