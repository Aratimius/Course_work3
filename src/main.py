"""Результат работы программы"""

import utils


data = utils.get_all_operations()
sorted_data = utils.get_sorted(data)
executed_data = utils.get_executed(sorted_data)

utils.get_five_last_operations(executed_data)

