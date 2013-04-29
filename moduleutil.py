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


import os
import sys
import subprocess


_simd = None


def check_output(cmd):
    """
    Reimplement this helper function from subprocess for backward
    compatability with Python 2.6
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = p.communicate()[0]
    rc = p.poll()
    return out, rc


def splitid(moduleid):
    """ Return the module and name from the moduleid """
    
    moduleid = moduleid.split('/',1)
    if len(moduleid) == 1:
        moduleid.append('')
    return moduleid[0],moduleid[1]


def print_centered(string,term_width=80,pad_char='~'):
    """ Print a string centered in the terminal """

    print >>sys.stderr, (' '+string+' ').center(term_width,pad_char)


def print_columns(moduleids,term_width=80):
    """ Print a list of strings in columns """

    if not moduleids: return;

    # Calculate the number of columns based on the longest string
    column_width = max(len(moduleid) for moduleid in moduleids)+2
    num_columns = term_width/column_width
    column_length = (len(moduleids)+num_columns-1)/num_columns

    # Pad the moduleid with spaces
    moduleids = [moduleid.ljust(column_width) for moduleid in moduleids]

    # Print in columns
    for i in range(column_length):
        line = ''
        for j in range(num_columns):
            k = j*column_length+i
            if k < len(moduleids):
                line += moduleids[k]
        print >>sys.stderr, line


def simdize(path):
    """
    Replace the special value `%SIMD%` in `path` with the highest SSE
    instruction level of the current machine, in the set:

        (`avx`, `sse4.2`, `sse4a`, `sse3`, `.`)
    """
    global _simd
    if _simd is None:

        if os.path.exists('/proc/cpuinfo'):

            cmd = ['grep', '-m', '1', 'flags', '/proc/cpuinfo']
            flags, rc = check_output(cmd)

            if rc:
                print >>sys.stderr, \
                    "module: warning: couldn't grep /proc/cpuinfo"
                _simd = '.'

            else:
                if ' avx ' in flags:        _simd = 'avx'
                elif ' sse4_2 ' in flags:   _simd = 'sse4.2'
                elif ' sse4a ' in flags:    _simd = 'sse4a'
                elif ' sse3 ' in flags:     _simd = 'sse3'
                else:                       _simd = '.'

        else:
            _simd = '.'

    return path.replace('%SIMD%', _simd)


def info(msg):
    """
    Print an informational message to stderr, prefixed with "module: ".
    """
    print >>sys.stderr, "module:", msg


# vim:ts=4:shiftwidth=4:expandtab:
