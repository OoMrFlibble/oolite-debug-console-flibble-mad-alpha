This will build an app tarball, with an executable that will work where python
 is unavailable.

It is aimed at Debian/Ubuntu systems.

It should work on other dists if the requirements are met.

Short version:

First, On Debian systems, we can check/install dependencies.

    ./make.sh debdeps

Then, make the tarball in fastest mode.

    ./make.sh onedir


To install to .local in a home directory:

    tar -C $HOME/.local/ -xpzf OoDC-*-linux-*-onedir.tar.gz

If rebuilding for any reason, delete the build directory.

    ./make.sh clean


Detailed info:

The script needs to be in the build tree at ./Linux/make.sh

It expects to be executed in that directory.

If run as:_

    ./make.sh debdeps

To build onedir version, which runs the fastest.

    ./make.sh onedir

To build onefile version, which runs the slowest, but is arguably tidier.

    ./make.sh onefile

Other args, clean (remove build dir), dist builds both onefile and onedir.

Any arg2 will be used as the base name for the tarball. Take care!
Any arg3 will be used as a destination directory for the tarballs.

In either of the build modes, it will:
    Create a "build" directory.
    Create a python3 venv in it.
    Activate the venv.
    Use pip inside the venv to install python dependencies and pyinstaller.
    Compile an executable of the project.
    Make an 'installable' tarball.

One other option, "desktop", will emit the content for a .desktop file.
This may be of use to anyone wanting to add a shebang line (#!/bin/env python3)
 into the source to execute it directly where requirements are satisfied.
    ./make desktop
