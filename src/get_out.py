from Course_work3.src.get_EXECUTED import get_executed


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
    account = data['to'][data['to'].find(first_number) + 1:]
    hidden_account = '**' + account[-4:]  # Счет

    if 'from' in data.keys():
        first_number = ''
        for letter in data['from']:
            if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                first_number = letter
                break
        card = data['from'][:data['from'].find(first_number)-1]  # Карта(Mastercard, Visa...)

        number = data['from'][data['from'].find(first_number):]

        hidden_number = number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]  # Номер


        return f"""{date} {data['description']}
{card} {hidden_number} -> Счет {hidden_account}
{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"""
    else:
        return f"""{date} {data['description']}
Счет {hidden_account}
{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"""
