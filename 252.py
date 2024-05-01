import math
def convert(numbers):
    return (math.sqrt(numbers.real**2 + numbers.imag**2), math.atan2(numbers.imag, numbers.real))
