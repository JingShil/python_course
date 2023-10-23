def get_pins(observed):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    def generate_pins(prefix, remaining_digits):
        if not remaining_digits:
            return [prefix]
        digit = remaining_digits[0]
        rest_digits = remaining_digits[1:]
        pins = []
        for neighbor in adjacent_digits[digit]:
            pins.extend(generate_pins(prefix + neighbor, rest_digits))
        return pins
    
    return generate_pins('', observed)