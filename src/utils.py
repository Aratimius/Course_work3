import json
import pathlib
from pathlib import Path


def get_all_operations():
    '''Прочитает файл .json и вернет содержимое'''

    with open(str(Path(pathlib.Path.cwd(), 'operations.json')), 'r', encoding='utf-8') as file:
        all_operations = json.loads(file.read())

        return all_operations


def get_sorted(operations):
    ''' Сортировка данных по дате
    От самого позднего к самому раннему'''

    new_data = []
    for operation in operations:
        if 'date' not in operation.keys():
            continue
        else:
            new_data.append(operation)

    sorted_data = sorted(new_data, key=lambda operation: operation['date'], reverse=True)

    return sorted_data


def get_executed(operations):
    '''Возвращает список свежих данных только в состоянии EXECUTED
    в колличестве 5 штук'''

    count = 0
    new_data = []

    for operation in operations:
        if operation['state'] == 'EXECUTED':
            new_data.append(operation)
            count += 1
        if count == 5:
            return new_data

    return new_data


def get_out(data):
    ''' Правильное представление данных'''

    date = data['date'][:data['date'].find('T')]  # обрежем строку, оставив только дату
    date_list = date.split('-')
    date = '.'.join(date_list[::-1])  # Дата

    first_number = ''
    for letter in data['to']:
        if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            first_number = letter
            break
    account = data['to'][data['to'].find(first_number):]
    account_name = data['to'][:data['to'].find(first_number)-1] # Счет или название карты получателя
    if account_name == 'Счет':
        hidden_account = '**' + account[-4:]  # Счет
    else:
        hidden_account = account[:4] + ' ' + account[4:6] + '** **** ' + account[-4:]

    if 'from' in data.keys():
        first_number = ''
        for letter in data['from']:
            if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                first_number = letter
                break
        card = data['from'][:data['from'].find(first_number) - 1] # Счет или Карта отправителя
        number = data['from'][data['from'].find(first_number):]
        if card == 'Счет':
            hidden_number = '**' + number[-4:]
        else:
            hidden_number = number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]  # Номер

        return f"""{date} {data['description']}
{card} {hidden_number} -> {account_name} {hidden_account}
{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"""
    else:
        return f"""{date} {data['description']}
Счет {hidden_account}
{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"""


def get_five_last_operations(operations):
    """ Вывод пяти последних операций в правильном формате"""

    for operation in operations:
        result = get_out(operation)
        print(result, '\n')
