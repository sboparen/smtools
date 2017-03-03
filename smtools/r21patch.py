#!/usr/bin/env python2
import argparse
import hashlib
import os
import shutil
import subprocess


def smoggpaths(songdir):
    smpaths = []
    oggpaths = []
    for name in os.listdir(songdir):
        path = os.path.join(songdir, name)
        if path.lower().endswith('.sm'):
            smpaths.append(path)
        if path.lower().endswith('.ogg'):
            oggpaths.append(path)
    if len(smpaths) != 1:
        assert False, '%s has %d sm files' % (songdir, len(smpaths))
    if len(oggpaths) != 1:
        assert False, '%s has %d ogg files' % (songdir, len(oggpaths))
    smpath, = smpaths
    oggpath, = oggpaths
    return smpath, oggpath


def shrinkogg(oggdest, rate):
    with open(oggdest, 'rb') as f:
        h = hashlib.md5(f.read() + str(rate)).hexdigest()
    path = os.path.join(os.getenv('HOME'), '.smtools')
    if not os.path.exists(path):
        os.mkdir(path)
    oggpath = os.path.join(path, '%s.ogg' % h)
    if not os.path.exists(oggpath):
        wavpath = os.path.join(path, '%s.wav' % h)
        cmd = ['oggdec', oggdest, '-o', wavpath]
        subprocess.check_call(cmd)
        cmd = ['oggenc', wavpath, '-b', str(rate), '-o', oggpath + '.tmp']
        subprocess.check_call(cmd)
        os.unlink(wavpath)
        os.rename(oggpath + '.tmp', oggpath)
    shutil.copyfile(oggpath, oggdest)


def r21patch(songdir, destpath):
    smpath, oggpath = smoggpaths(songdir)
    smdest = os.path.join(destpath, os.path.basename(smpath))
    oggdest = os.path.join(destpath, os.path.basename(oggpath))
    shutil.copyfile(smpath, smdest)
    shutil.copyfile(oggpath, oggdest)
    if os.path.getsize(smdest) > 100e3:
        assert False, '%s sm file is too big' % songdir
    if os.path.getsize(oggdest) > 5e6:
        shrinkogg(oggdest, 96)
        if os.path.getsize(oggdest) > 5e6:
            print 'warning: %s ogg file still too big' % songdir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('songdirs', nargs='+')
    parser.add_argument('--destroot', '-d', required=True)
    args = parser.parse_args()
    for songdir in args.songdirs:
        path = os.path.dirname(songdir)
        songname = os.path.basename(path)
        path = os.path.dirname(path)
        packname = os.path.basename(path)
        destpath = os.path.join(args.destroot, packname)
        if not os.path.exists(destpath):
            os.mkdir(destpath)
        destpath = os.path.join(destpath, songname)
        if not os.path.exists(destpath):
            os.mkdir(destpath)
        r21patch(songdir, destpath)


if __name__ == '__main__':
    main()
