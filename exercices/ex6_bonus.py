import re
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

def replace_txt(censored,sample):
    list_len=len(CENSORED_WORDS)
    print(f"", list_len)
    for i in range(0,list_len):
        sample = re.sub(censored[i], bcolors.RED +'xxxxxxxxx'+ bcolors.ENDC, sample)
        i=+1
    return sample

def main():
  sample_text = "jbfkjbjfkz fdfzefzefze fzef poi mlk nbv fzefzefz effff"
  print(replace_txt(CENSORED_WORDS,sample_text))

if __name__ == "__main__":
  main()  

