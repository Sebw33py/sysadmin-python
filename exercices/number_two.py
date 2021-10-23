import fileinput, os, shutil, sys
from typing import Tuple, Dict, List
# assert ('linux' in sys.platform), "Function can only run on Linux systems."


def replace_characters_in_text_file(path: str, char: str, to_replace: Tuple[str]):
    try:
        for line in fileinput.input(path, inplace=True):
            for x in to_replace:
                line = line.replace(x, char)
            print(line, end="")
    except FileNotFoundError:
        print(f"Fichier non-trouvé: {path}")
    except Exception as ex:
        print(f"Exception: {ex}")


def return_text_file_into_list(path: str) -> List[Dict[int, str]]:
    ret_list: List = list() # = () is the same
    i: int = 0
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                i += 1
                # rstrip() removes '\n'
                line = line.rstrip()
                ret_list.append(
                    {
                        "line_number": i,
                        "line": line,
                        "char_number": len(line)
                    }
                )
    except FileNotFoundError:
        print(f"Fichier non-trouvé: {path}")
    except Exception as ex:
        print(f"Exception: {ex}")
    return ret_list

def display_line_number_and_text_from_list(text_list: List[Dict[int, str]]):
    for item in text_list:
        try:
            print(
                f"Ligne numéro {item['line_number']}: {item['char_number']} caractères--> {item['line']}"
            )
        except KeyError as ke:
            print(f"Key {ke} does not exist ...")

def main():
    path = "./statics/edit-text-copy.txt"
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    shutil.copy2("./statics/edit-text.txt", path)
    replace_characters_in_text_file(
        path, "x", ("c", "f", "g", "e", "w", "W")
    )
    returned_lines = return_text_file_into_list(path)
    display_line_number_and_text_from_list(returned_lines)

    # Works as well !
    # display_line_number_and_text_from_dict(
    #   return_text_file_into_tuple(path)
    # )


if __name__ == '__main__':
    main()