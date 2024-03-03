import json
from datetime import datetime as dt

def get_date(x, format="%Y-%m-%dT%H:%M:%S.%f"):
    return dt.strptime(x.get("date"), format)


def print_bank_account(operation_from):
    '''
    Функция для конвертирования номера счёта отправителя по маске
    1111 11** **** 1111 для карт (16-значные номера)
    **1111 для счетов (20-значные номер)
    '''
    number = operation_from.split()[-1] # с помощью split получаем номер

    if len(operation_from.split()) == 3: # если в строке 3 слова (например Visa Gold {номер}), то надо будет вывести полное название карты
        if len(number) == 16: # если номер состоит из 16 символов
            print(f"{operation_from.split()[0]} {operation_from.split()[1]}"
                  f" {number[:4]} {number[4:6]}** **** **** {number[-4:]}", end=' ') # с помощью срезов добиваемся результата

        else: # если номер состоит НЕ из 16 символов, то выводим по маске счёта
            print(f"Счет **{number[-4:]}", end=' ')

    else: # соответственно, если в строке всего два слова, то в названии только одно первое
        if len(number) == 16:  # если номер состоит из 20 символов
            print(f"{operation_from.split()[0]} {number[:4]} {number[4:6]}** **** **** {number[-4:]}",
                  end=' ')  # с помощью срезов добиваемся результата

        else:  # если номер состоит НЕ из 16 символов, то выводим по маске счёта
            print(f"Счет **{number[-4:]}", end=' ')


with open('operations.json', encoding='UTF-8') as file:
    json_file = json.load(file) # открываем файл и считываем значение

operations = [operation for operation in json_file if operation.get('id')] # получаем новый список БЕЗ пустого объекта
operations = sorted(operations, key=lambda operation: dt.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                    reverse=True)[:5] # сортируем по дате


for operation in operations:
    if operation.get('id'): # проверяем существование операции (мы не попадёмся на ваши пустые записи {} !!!)
        operation['date'] = dt.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        if operation.get('from'): # отправителя может и не быть, т.к. есть операции по открытию счетов
            print(f"{operation['date'].strftime('%d.%m.%Y')} {operation['description']}") # ну а дальше вывод
            print_bank_account(operation['from'])
            print("->", end=' ')
            print_bank_account(operation['to'])
            print(f"\n{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")

        else:
            print(f"{operation['date'].strftime('%d.%m.%Y')} {operation['description']}")
            print_bank_account(operation['to'])
            print(f"\n{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")

