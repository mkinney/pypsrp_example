#!/usr/bin/env python

import sys


from pypsrp.client import Client


def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)


if __name__ == '__main__':
    arg_check()

    server = sys.argv[1]
    client = Client(server, username="vagrant", password="vagrant", ssl=False)

    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("dir")
    print("stdout:{}".format(stdout))
    print("stderr:{}".format(stderr))
    print("rc:{}".format(rc))
