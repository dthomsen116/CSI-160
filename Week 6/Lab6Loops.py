phone_numbers = ['555-1212', '999-0738']


def add_area_code(phone_numbers, area_code):

    return area_code + phone_numbers


with_area_code = add_area_code(phone_numbers[0], '(802) ')

print(with_area_code)