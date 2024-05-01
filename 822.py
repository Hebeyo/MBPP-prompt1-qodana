def pass_validity(p):
    import re
    if (len(p)<6 or len(p)>12):
        return False
    if not re.search("[a-z]",p):
        return False
    if not re.search("[0-9]",p):
        return False
    if not re.search("[A-Z]",p):
        return False
    if not re.search("[$#@]",p):
        return False
    if re.search("\s",p):
        return False
    return True
