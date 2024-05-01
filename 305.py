def start_withp(words):
    for word in words:
        if word.startswith('p') or word.startswith('P'):
            p = word.split()
            return (p[0], p[1])
