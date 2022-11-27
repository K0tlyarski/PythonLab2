from email import generator
import os


def get_next_element(class_mark: str) -> generator:
    path = os.path.join("dataset", class_mark)
    names_list = os.listdir(path)
    names_list.append(None)
    mygenerator = (item for item in names_list)
    for i in mygenerator:
        yield i
