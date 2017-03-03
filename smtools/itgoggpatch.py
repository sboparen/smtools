#!/usr/bin/env python2
import os
import sys


def main():
    os.chdir(os.path.dirname(__file__))
    os.execvp('./itgoggpatch', sys.argv)


if __name__ == '__main__':
    main()
