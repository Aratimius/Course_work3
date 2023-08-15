from Course_work3.src.get_EXECUTED import get_executed


def test_get_executed():
    assert get_executed([{'state': 'EXECUTED', 'id': '1'}, {'state': 'CANCELED', 'id': '2'}]) == \
           [{'state': 'EXECUTED', 'id': '1'}]

    assert get_executed([{'state': 'EXECUTED', 'id': '1'}, {'state': 'EXECUTED', 'id': '2'},
                         {'state': 'EXECUTED', 'id': '3'}, {'state': 'EXECUTED', 'id': '4'},
                         {'state': 'EXECUTED', 'id': '5'}, {'state': 'EXECUTED', 'id': '6'}]) == \
           [{'state': 'EXECUTED', 'id': '1'}, {'state': 'EXECUTED', 'id': '2'},
            {'state': 'EXECUTED', 'id': '3'}, {'state': 'EXECUTED', 'id': '4'},
            {'state': 'EXECUTED', 'id': '5'}]
