import socket


def check_port(server, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    result = sock.connect_ex((server, port))

    if result == 0:
        port_is_opened = True
    else:
        port_is_opened = False

    sock.close()

    return port_is_opened


def check_ports(server, start_port, end_port, timeout):
    opened_ports = []
    for port in range(start_port, end_port + 1):
        port_is_opened = check_port(server, port, timeout)
        if port_is_opened:
            print(f"JACKPOT!!! PORT {port} IS OPENED!!!")
            opened_ports.append(port)
        else:
            print(f"Port {port} is closed")
    return opened_ports


def main():
    # Define the server to test against
    server = "portquiz.net"

    # Define the range of ports you want to check
    start_port = 1
    end_port = 49151

    # Timeout for the connection attempt
    timeout = 0.1 # in seconds

    opened_ports = check_ports(server, start_port, end_port, timeout)
    print(f"Opened ports: {opened_ports}")


if __name__ == "__main__":
    main()
