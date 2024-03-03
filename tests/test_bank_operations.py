from src.bank_operations import formatted_bank_account


def test_formatted_bank_account():
    assert formatted_bank_account('Счет 59956820797131895975') == 'Счет **5975'
    assert formatted_bank_account('МИР 8665240839126074') == 'МИР 8665 24** **** 6074'
    assert formatted_bank_account('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    # assert formatted_bank_account('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
