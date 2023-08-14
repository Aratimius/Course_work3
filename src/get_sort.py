from Course_work3.src.read_file import get_all_operations


def get_sorted():
    ''' Сортировка данных по дате
    От самого позднего к самому раннему'''

    data = get_all_operations()
    sorted_data = sorted(data, key=lambda operation: operation['date'], reverse=True)

    return sorted_data
print(get_sorted())