#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Debug \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DWITH_PYTHONQT=OFF \
                          -DINSTALL_CONFIG=ON \
                          -DWITH_CRASHREPORTER=ON", \
                          sourceDir=".." )
    
def build():
    shelltools.cd("build")
    
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    
    #pisitools.insinto("/usr/share/calamares", "../settings.conf")
    #pisitools.insinto("/usr/share/calamares/modules", "src/modules/machineid/machineid.conf")
    
    #dbus configuration for pisi
    pisitools.dosed("%s/usr/share/calamares/modules/machineid.conf" % get.installDIR(), "systemd: true", "systemd: false")
    pisitools.dosed("%s/usr/share/calamares/modules/machineid.conf" % get.installDIR(), "symlink: true", "symlink: false")
    
    
    
    pisitools.dodoc("../README.*")
