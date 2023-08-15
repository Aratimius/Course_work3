from Course_work3.src.get_out import get_out


def test_get_out():
    assert get_out({
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }) == """12.09.2018 Перевод организации
Visa Platinum 1246 37** **** 3588 -> Счет **1657
67314.70 руб."""