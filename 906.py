def extract_date(url):
    import re
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
