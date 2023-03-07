import fileinput

def replace_txt(CENSORED_WORDS,path):
    with fileinput.input(files=path, inplace=True, backup='.orig') as f:
        for ip_line in f:
            op_line = ip_line.replace(CENSORED_WORDS, 'x')
            print(op_line, end='')
    return True
