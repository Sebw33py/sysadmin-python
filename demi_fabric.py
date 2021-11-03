from fabric import Connection, SerialGroup


def run_hostname(host: list):
    # Connect to several hosts
    result = SerialGroup("host2", "host1").run("hostname")
    print(result)
    result = ThreadingGroup("host2", "host1").run("hostname")
    print(result)

def main():
    host = "localhost"
    # Connect to one host
    result = Connection(host).local("hostname")
    # Use run() for non-local operations
    # Connection("myhost").run("hostname")
    print(result)
    with Connection(host) as con:
        if con.is_connected:
            con.local(host)
            # con.run("hostname")
            con.get(
                "/Users/Alexandre/file_to_download.txt",
                "."
                )
        else:
            print(f"Error connecting to host {host}")

    run_hostname(["host1", "host2"])

if __name__ == "__main__":
    main()