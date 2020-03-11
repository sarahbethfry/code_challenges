def fit_to_width(sentence, maxnum):
    str_line = ""
    acc = 0
    for char in sentence:
        acc += 1
        str_line += char
        if (char==" ") and (acc > maxnum): 
            acc = 0
            str_line += "\n"
    print(str_line)
       
