import mymodtxt.txt_module as sp
import argparse
import pathlib


CENSORED_WORDS = "b"

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
    sp.replace_txt(CENSORED_WORDS,args.str)
  except ValueError:
      return "not correct"
  
if __name__ == "__main__":
  main()