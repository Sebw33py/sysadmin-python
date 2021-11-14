from fabric import Connection, SerialGroup, ThreadingGroup


def run_hostname(*hosts):
    # Connect to several hosts
    result = SerialGroup(*hosts).run("hostname")
    print(result)
    result = ThreadingGroup(*hosts).run("hostname")
    print(result)

def main():
    with Connection("localhost") as con:
        con.local("hostname", replace_env=False)
    run_hostname(
        "localhost",
        "AlexandreRaspaud@192.168.1.166"
    )

if __name__ == "__main__":
    main()