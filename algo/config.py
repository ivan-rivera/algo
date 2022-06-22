"""Configurations"""
import configparser
import pathlib
import logging
import sys


def _infer_project_path() -> pathlib.Path:
    """
    Fetch the absolute path of the project
    Returns
        Path to the project
    """
    return pathlib.Path(__file__).parent.parent.resolve()


PROJECT_DIR = _infer_project_path()
config = configparser.ConfigParser()
config.read(PROJECT_DIR / "config.ini")
PROJECT_NAME = config["meta"]["project-name"]

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(PROJECT_NAME)
