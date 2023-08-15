from Course_work3.src.read_file import get_all_operations


def get_sorted(data = get_all_operations()):
    ''' Сортировка данных по дате
    От самого позднего к самому раннему'''

    new_data = []
    for operation in data:
        if 'date' not in operation.keys():
            continue
        else: new_data.append(operation)

    sorted_data = sorted(new_data, key=lambda operation: operation['date'], reverse=True)

    return sorted_data
