import csv
import os


class IteratorTask1:
    def __init__(self, path: str):
        self.file_names = os.listdir(os.path.join('dataset', path))
        self.counter = 0
        self.limit = len(self.file_names)
        self.path = path

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration


class IteratorTask2:
    def __init__(self, class_name: str,  path: str):
        self.file_names = os.listdir(os.path.join(path))
        for name in self.file_names:
            if not class_name in name:
                self.file_names.remove(name)

        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration


class IteratorTask3:
    def __init__(self, class_name: str,  path: str, annotation_name: str):
        self.file_names = list()
        with open(os.path.join(path, annotation_name)) as file:
            reader = csv.reader(file, delimiter=',')
            for file_info in reader:
                if file_info[1] == class_name:
                    self.file_names.append()
        for name in self.file_names:
            if not class_name in name:
                self.file_names.remove(name)

        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration