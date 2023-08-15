from Course_work3.src.get_sort import get_sorted

def test_get_sorted():
    assert get_sorted()[0] == {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}
    assert get_sorted()[99] == {'id': 317987878, 'state': 'EXECUTED', 'date': '2018-01-13T13:00:58.458625', 'operationAmount': {'amount': '55985.82', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 8906171742833215', 'to': 'Visa Platinum 6086997013848217'}
    assert get_sorted([{}, {'date': 1}]) == [{'date': 1}]