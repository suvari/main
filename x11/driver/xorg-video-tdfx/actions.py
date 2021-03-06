#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("\
                         --disable-static \
                         --disable-dri \
                        ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "ChangeLog", "README*")
