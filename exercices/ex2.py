import fileinput
import sys
import argparse

CENSORED_WORDS = "b"
TPATH=sys.argv[1]

def replace_txt(CENSORED_WORDS):
    with fileinput.input(files=TPATH, inplace=True, backup='.orig') as f:
        for ip_line in f:
            op_line = ip_line.replace(CENSORED_WORDS, 'x')
            print(op_line, end='')    
        
def main():
  print(replace_txt(CENSORED_WORDS,TPATH))

if __name__ == "__main__":
  main()