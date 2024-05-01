def extract_values(text):
    text = text.split(',')
    result = []
    for i in text:
        result.append(i.strip()[1:-1])
    return result
