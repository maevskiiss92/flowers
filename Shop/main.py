_str = 'abc-15def4gh42klmno'

def super_function(_str: str) -> list[int]:
    for ch in _str:
        if not (ch.isdigit() or ch == '-'):
            _str = _str.replace(ch, '#')
    while '##' in _str:
        _str = _str.replace('##', '#')
    number = max([int(el) for el in _str.split('#') if el != ''])
    return number

result = super_function(_str=_str)
print(result)