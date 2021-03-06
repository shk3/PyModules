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

### MODIFY THESE ###

# Set this to the root directory where all software packages will be installed.
# PyModules enforces the convention that you install all packages to:
#   <rootdir>/<package-name>/<package-version>
rootdir = '/gpfs/runtime/opt/'

# Forces all modulefiles to have group-writable permissions: important if you
# plan to have multiple users maintaining modulefiles and updating the
# database. NOTE: you must include the leading 0 in the octal code!
moduleperm = 0664

### DO NOT EDIT BELOW ###

# Default data.

defaults = {
    'rootdir': os.path.join(rootdir, '%(name)s', '%(__name__)s'),
    'version': '%(__name__)s',
    'default': 'false'
}

messages = {
	'unknown': """
  Please contact CCV support (support@ccv.brown.edu) if you think that software
  with this module name should be installed."""
}

# Environment variables.

MODULEPATH = os.environ['MODULEPATH']
MODULEDB = os.path.join(MODULEPATH, '.db.sqlite')
MODULESHELL = os.environ['MODULESHELL']
LOADEDMODULES = 'LOADEDMODULES'

