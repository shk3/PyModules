#
# PyModules - Software Environments for Research Computing Clusters
#
# Copyright 2012-2013, Brown University, Providence, RI. All Rights Reserved.
#
# This file is part of PyModules.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose other than its incorporation into a
# commercial product is hereby granted without fee, provided that the
# above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation, and that the name of Brown University not be used in
# advertising or publicity pertaining to distribution of the software
# without specific, written prior permission.
#
# BROWN UNIVERSITY DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
# PARTICULAR PURPOSE.  IN NO EVENT SHALL BROWN UNIVERSITY BE LIABLE FOR
# ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


import sys
import argparse

from module import ModuleError, ModuleDb
from modulecfg import MODULEPATH

def _rebuild(args):
    # Rebuild the module database from modulefiles in the path

    moduledb = ModuleDb()
    moduledb.rebuild(args.modulepath)


def _insert(args):
    # Insert each modulefile into the database

    moduledb = ModuleDb()
    for modulefile in args.modulefile:
        moduledb.insert(modulefile,args.force)


def main():

    parser = argparse.ArgumentParser(prog='moduledb')
    subparsers = parser.add_subparsers(title='subcommands')

    rebuild_parser = subparsers.add_parser('rebuild')
    rebuild_parser.add_argument('modulepath',nargs='?',default=MODULEPATH)
    rebuild_parser.set_defaults(func=_rebuild)

    insert_parser = subparsers.add_parser('insert')
    insert_parser.add_argument('-f','--force',action='store_true');
    insert_parser.add_argument('modulefile',nargs='+')
    insert_parser.set_defaults(func=_insert)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()

# vim:ts=4:shiftwidth=4:expandtab:
