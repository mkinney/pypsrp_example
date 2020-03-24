#!/usr/bin/env python

import sys


from pypsrp.shell import Process, SignalCode, WinRS
from pypsrp.wsman import WSMan


def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)


if __name__ == '__main__':
    arg_check()

    server = sys.argv[1]
    ps = sys.argv[2]

    # creates a http connection with no encryption and basic auth
    wsman = WSMan(server, ssl=False, auth="basic", encryption="never",
                  username="vagrant", password="vagrant")

    with WinRS(wsman) as shell:
        # execute a process with arguments in the background
        process = Process(shell, ps)
        process.begin_invoke()  # start the invocation and return immediately
        process.poll_invoke()  # update the output stream
        process.end_invoke()  # finally wait until the process is finished
        process.signal(SignalCode.CTRL_C)
        print('stdout', process.stdout)
        print('stderr', process.stderr)
        print('rc', process.rc)
