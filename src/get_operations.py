from Course_work3.src.get_out import get_out
from Course_work3.src.get_EXECUTED import get_executed

def get_five_last_operations(date = get_executed()):
    """ Вывод пяти последних операций в правильном формате"""

    for operation in date:
        result = get_out(operation)
        print(result, '\n')
