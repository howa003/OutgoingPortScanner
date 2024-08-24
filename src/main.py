import socket


def check_port(server, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)  # Set a timeout for the connection attempt

    result = sock.connect_ex((server, port))

    if result == 0:
        port_is_opened = True
    else:
        port_is_opened = False

    sock.close()

    return port_is_opened


def check_ports(server, start_port, end_port):
    opened_ports = []
    for port in range(start_port, end_port + 1):
        port_is_opened = check_port(server, port)
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

    opened_ports = check_ports(server, start_port, end_port)
    print(f"Opened ports: {opened_ports}")


if __name__ == "__main__":
    main()
