from Course_work3.src.get_sort import get_sorted


def get_executed(data=get_sorted()):
    '''Возвращает список свежих данных только в состоянии EXECUTED
    в колличестве 5 штук'''

    count = 0
    new_data = []

    for operation in data:
        if operation['state'] == 'EXECUTED':
            new_data.append(operation)
            count += 1
        if count == 5:
            return new_data

    return new_data
