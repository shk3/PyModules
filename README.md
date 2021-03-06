PyModules is an alternative implementation of the
[Environment Modules](http://modules.sourceforge.net/) system
for managing software environments on research computing clusters.
It provides several new features:

* Uses simple, INI-style configuration files that share common values across
  multiple versions of a package.
* Module configuations are cached in a SQLite database, and editing/publishing
  are separate actions.
* Modules can be categorized. The `module avail` command lists by
  category or by fulltext search on the package name or version.
* Modules can be localized by CPU architecture, for either a specific vendor
  (AMD vs. Intel), SSE instruction set, or CPU model identifier.
* New `module bin` command lists all binaries provided by a module.

PyModules is developed by the
[Center for Computation and Visualization](http://ccv.brown.edu/)
at Brown University, and distributed freely for academic use under a
non-commercial license (see the LICENSE file for full details).

## Installation

Zip archives are available from the [downloads
page](https://bitbucket.org/mhowison/pymodules/downloads), or you can clone the
Bitbucket repo for the latest development version.

For installation instructions, see the INSTALL file.

## Documentation

See [http://ccv.brown.edu/mhowison/pymodules](http://ccv.brown.edu/mhowison/pymodules)

## Citing

Howison M, Shen A, Loomis A. 2013. Building Software Environments for Research
Computing Clusters. In Proceedings of the 27th Large Installation System
Administration Conference (LISA '13), Washington, DC, USA.
[https://www.usenix.org/conference/lisa13/building-software-environments-research-computing-clusters](https://www.usenix.org/conference/lisa13/building-software-environments-research-computing-clusters)

## Issues

Please report any issues using the issue tracker at Bitbucket:

[https://bitbucket.org/mhowison/pymodules/issues](https://bitbucket.org/mhowison/pymodules/issues)

## Authors
Mark Howison  
Andy Loomis  
Aaron Shen

