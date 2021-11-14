import argparse

def display(*values) -> bool:
    for value in values:
        print(value)
    return True

def main():
    parser = argparse.ArgumentParser(
        prog='DEMO_ARGPARSE',
        description="Script d'Alexandre",
        exit_on_error=False
    )
    parser.add_argument("--version",action="version", version="%(prog)s 1.0.1")
    # Positionnal argument
    parser.add_argument("text", type=str, help="Texte à afficher")
    parser.add_argument(
        "integer", metavar="N",
        type=int, nargs="+",
        help="Valeurs à afficher"
    )
    # Flag argument
    parser.add_argument('--flag', action=argparse.BooleanOptionalAction, default=False)
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as ex:
        # Display the argument who caused the error
        print(ex.args)
        print(f"Attention ! Seulement des nombres sont autorisés ; votre input --> {ex.args[-1].split()[-1]}")
        return
    if display(*args.text, *args.integer, *[args.flag]):
        print("Tout s'est bien passé!")

if __name__ == "__main__":
    main()