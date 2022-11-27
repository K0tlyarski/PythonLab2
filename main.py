from Task1 import run1
from Task2 import run2
from Task3 import run3
from Task4 import get_next_element

if __name__== '__main__':
    run1('tiger', 'annotation1.csv')
    run2('datasetcopy1', 'annotation.csv')
    run3('annotation.csv', 'datasetcopy2')


    for item in get_next_element('tiger'):


        print(item)