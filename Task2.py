import shutil
import os
import csv


def create_dir(dir_name: str) -> str:
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name