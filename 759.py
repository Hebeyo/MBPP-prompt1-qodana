def is_decimal(num):
    if num.isdigit():
        return True
    num = num.split('.')
    if len(num) != 2:
        return False
    if not num[0].isdigit() or not num[1].isdigit():
        return False
    if len(num[1]) != 2:
        return False
    return True
