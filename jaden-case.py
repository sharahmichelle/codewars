def to_jaden_case(string):
    # ...
    words = string.split()
    jaden_cased = []
    
    for word in words:
        jaden_cased.append(word.capitalize())
    
    return " ".join(jaden_cased)