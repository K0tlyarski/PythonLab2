from email import generator
import random
import os
import shutil
from Task2 import create_dir
import csv

def get_element(class_name:str)->generator:
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name