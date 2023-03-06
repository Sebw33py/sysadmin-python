class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

CENSORED_WORDS = ["poi","mlk"]

def replace_censored(i, txt):
 for word in i:
   txt = txt.replace(word, bcolors.CYAN +"##########"+ bcolors.ENDC)
 return txt

def main():
  sample = "jbfkjbjfkz fdfzefzefze fzef poi mlk nbv fzefzefz effff"
  print(replace_censored(CENSORED_WORDS,sample))

if __name__ == "__main__":
  main()  