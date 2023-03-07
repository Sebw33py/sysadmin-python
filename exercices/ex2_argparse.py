import argparse
import fileinput
import pathlib

CENSORED_WORDS = "b"

def replace_txt(CENSORED_WORDS,path):
    with fileinput.input(files=path, inplace=True, backup='.orig') as f:
        for ip_line in f:
            op_line = ip_line.replace(CENSORED_WORDS, 'x')
            print(op_line, end='')
    return True

def main():
  parser = argparse.ArgumentParser(
      description="Replacing caracter script v0.1"
  )
  parser.add_argument(
      "str", metavar="path_to_file",
      type=pathlib.Path, help="Path to file example : colors.txt"
  )
  args = parser.parse_args()
  try:
    replace_txt(CENSORED_WORDS,args.str)
  except ValueError:
      return "not correct"
  
if __name__ == "__main__":
  main()