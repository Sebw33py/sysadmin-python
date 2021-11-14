from getpass import getpass
from fabric import Connection, SerialGroup, ThreadingGroup


def main():
    with Connection("localhost") as con:
        con.local("hostname", replace_env=False)

    password = getpass("Please enter AlexandreRaspaud@10.188.102.220's password:\n")
    result = Connection(
        "AlexandreRaspaud@10.188.102.220",
        connect_kwargs={
            "password": password,
        }
    ).run("uname -s")

if __name__ == "__main__":
    main()