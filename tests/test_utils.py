from Course_work3.src import utils


def test_get_all_operations():
    assert utils.get_all_operations()[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

    assert utils.get_all_operations()[99] == {}


def test_get_sorted():
    assert utils.get_sorted([{'date':'2'}, {'date':'1'}, {'date':'3'}]) ==\
           [{'date':'3'}, {'date':'2'}, {'date':'1'}]

    assert utils.get_sorted([{'date': '2'}, {'date': '1'}, {'date': '3'}, {}]) ==\
           [{'date':'3'}, {'date':'2'}, {'date':'1'}]


def test_get_executed():
    assert utils.get_executed([{'state':'EXECUTED'}, {'state':'1'}, {'state':'EXECUTED'}]) ==\
           [{'state':'EXECUTED'}, {'state':'EXECUTED'}]
    assert utils.get_executed([{'state':'EXECUTED'}, {'state':'EXECUTED'}, {'state':'EXECUTED'}, {'state':'EXECUTED'}, {'state':'EXECUTED'}, {'state':'EXECUTED'}]) ==\
        [{'state':'EXECUTED'}, {'state':'EXECUTED'}, {'state':'EXECUTED'},{'state':'EXECUTED'}, {'state':'EXECUTED'}]


def test_get_out():
    assert utils.get_out({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }) ==\
           """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб."""