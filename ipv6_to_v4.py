from ipaddress import IPv6Address, IPv4Address
from sys import stdin, stdout, stderr


def main(ip_str) -> str:
    try:
        ip: IPv6Address = IPv6Address(ip_str)
        ipv4: IPv4Address = ip.ipv4_mapped
        return str(ipv4)
    except Exception as e:
        print(f'ERROR converting {ip_str}: {e}', file=stderr)
        return ip_str


if __name__ == '__main__':
    for ipv6 in stdin:
        stdout.write(main(ip_str=ipv6.rstrip()))
