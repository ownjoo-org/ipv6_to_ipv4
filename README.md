# ipv6_to_ipv4

quick util to convert IPv6 addresses with embedded IPv4 addresses to their IPv4 string representations

# examples
```
$ echo '::ffff:192.168.0.1' | python ipv6_to_v4.py
192.168.0.1

$ echo '::ffff:192.168.0.1' | python ipv6_to_v4.py | cut -d '.' -f2
168
```
