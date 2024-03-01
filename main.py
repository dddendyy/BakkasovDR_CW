import json
import datetime


def print_operations_from(operation_from):
    number = operation_from.split()[-1]
    if len(number) == 20:
        print(f"{number[:4]} {number[4:6]}** **** **** {number[-4:]}", end=' ')

    else:
        print(f"{number[:4]} {number[4:6]}** **** {number[-4:]}", end=' ')


with open('operations.json', encoding='UTF-8') as file:
    operations = json.load(file)


for operation in operations:
    if operation.get('date'):
        if operation.get('from'):
            print(f"{operation['date']} {operation['description']}")
            print_operations_from(operation['from'])
            print(f"-> {operation['to']}")
            print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")

        else:
            print(f"{operation['date']} {operation['description']}\n"
                  f"{operation['to']}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")



