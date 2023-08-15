import json

def get_all_operations():
    '''Прочитает файл .json и вернет содержимое'''

    with open('/media/artur/Artur_files/PythonProjects/Course_work_3/operations.json', 'r') as file:
        operations = file.read()
        all_operations = json.loads(operations)

        return all_operations

