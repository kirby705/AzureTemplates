#!/usr/bin/env python

import os
import sys
import struct
import time
from opster import command, dispatch

header = struct.Struct('iii')

@command()
def replay(filename, factor=('f', 1, 'Speedup factor')):
    main(filename, 'replay', factor=factor)

@command()
def typing(filename):
    main(filename, 'typing')

@command()
def inspect(filename):
    main(filename, 'inspect')

def main(filename, action, factor=1):
    winid = int(os.getenv('WINDOWID'))

    script = open(filename)
    basetime = None
    prevtime = None
    stepnum = 0
    args = []
    while True:
        data = script.read(header.size)
        if not data:
            break
        sec, usec, n = header.unpack(data)
        curtime = sec + usec/1000000.0
        if basetime is None:
            basetime = prevtime = curtime
        delay = curtime-prevtime
        prevtime = curtime
        data = script.read(n)
        if action == 'inspect':
            print '%8.4f %4d %s' % (delay, n, `data[:40]`)
            continue
        if action == 'replay':
            time.sleep(delay/factor)
        elif action == 'typing':
            delay = 0
            if n == 1:
                delay = 0.2
            elif data.startswith('\r\n'):
                delay = 0.5
            if delay:
                os.system('import -window %s step%03d.gif' % (winid, stepnum))
                #time.sleep(delay)
                #print '-delay %d step%03d.gif' % (delay*100, stepnum),
                stepnum+=1

        sys.stdout.write(data)
        sys.stdout.flush()


if __name__ == '__main__':
    dispatch()
