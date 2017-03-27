#!/usr/bin/env python2
import os
import sys


def main():
    path = os.path.dirname(__file__)
    os.execvp(os.path.join(path, 'itgoggpatch'), sys.argv)


if __name__ == '__main__':
    main()
