import smtplib, ssl, argparse, re, pathlib, os
from email.message import EmailMessage


def email_regex(email: str) -> bool:
    return re.match(
        "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
        email
    )

def read_email_content(email: EmailMessage, path: str) -> EmailMessage:
    with open(path, "r") as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())
    return msg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='EMAIL_SENDER',
        description="Send email with your Gmail account.",
        exit_on_error=False
    )
    parser.add_argument("--version",action="version", version="%(prog)s 1.0.0")
    parser.add_argument("email", type=str, help="Your Gmail address")
    parser.add_argument("pwd", type=str, help="Your Gmail password")
    parser.add_argument("receiver", type=str, help="Receiver's email address")

    args = parser.parse_args()
    if not email_regex(args.email):
        raise ValueError(f"{args.email} invalid email address.")
    if not email_regex(args.receiver):
        raise ValueError(f"{args.receiver} invalid receiver's email address.")
    return args

def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    args = parse_args()
    port = 465  # For SSL
    email = read_email_content(
        EmailMessage(),
        os.path.join(root_file, "statics", "email_content.txt")
    )
    email["Subject"] = "Test email : Formation sysAdmin"
    email["From"] = args.email
    email["To"] = args.receiver

    context = ssl._create_unverified_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(args.email, args.pwd)
            # server.sendemail() is also available if you don't use EmailMessage class
            server.send_message(email)
            print(f"Email has been sent to {args.receiver} from {args.email}.")
    except Exception as ex:
        print(f"Email has NOT been sent : {ex}")

if __name__ == "__main__":
    main()