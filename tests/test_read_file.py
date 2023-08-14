from Course_work3.src.read_file import get_all_operations

def test_get_all_operations():
    operations = get_all_operations()
    assert operations[0] == {'date': '2019-08-26T10:50:58.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596837868705199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 64686473678894779589'}