#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#shelltools.export("PYTHONDONTWRITEBYTECODE", "")
shelltools.export("PYTHON", "/usr/bin/python3")

def setup():

    #temporary workaround for error: "'UINT64_C' was not declared in this scope"
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-G 'Ninja' \
		                  -D CMAKE_BUILD_TYPE=Release \
                          -D CMAKE_INSTALL_PREFIX=/usr \
                          -D CMAKE_INSTALL_LIBDIR=lib \
                          -D CMAKE_SKIP_RPATH=ON \
                           DESTDIR=%s  \
                          -DBUILD_EXAMPLES=1 \
                          -DINSTALL_C_EXAMPLES=1 \
                          -DINSTALL_PYTHON_EXAMPLES=1 \
                          -DINSTALL_OCTAVE_EXAMPLES=1 \
                          -DWITH_FFMPEG=0 \
                          -DWITH_UNICAP=0 \
                          -DENABLE_OPENMP=0 \
                          -DNEW_PYTHON_SUPPORT=1 \
                          -DOCTAVE_SUPPORT=0 \
                          -DUSE_MMX=1 \
                          -DUSE_SSE2=1 \
                          -DUSE_SSE3=0 \
                          -DUSE_SSE=1 \
                          -DWITH_TBB=ON \
                          -DWITH_EIGEN=ON \
                          -DWITH_1394=1 \
                          -DWITH_GSTREAMER=1 \
                          -DWITH_GTK=1 \
                          -DWITH_JASPER=1 \
                          -DWITH_JPEG=1 \
                          -DWITH_PNG=1 \
                          -DWITH_TIFF=1 \
                          -DWITH_V4L=1 \
                          -DWITH_XINE=1 \
                          -DWITH_VTK=OFF \
                          -DWITH_QT=OFF \
                          -DWITH_OPENGL=ON \
                          -DWITH_OPENCL=ON \
                          -DWITH_VULKAN=ON \
                          -DCMAKE_SKIP_RPATH=1 \
                          -DBUILD_opencv_python3=ON \
                          -DBUILD_opencv_python2=OFF \
                          -DBUILD_IPP_IW=OFF \
                          -DBUILD_ITT=OFF \
                          -DBUILD_JAVA=OFF \
                          -DBUILD_PROTOBUF=ON \
                          -DBUILD_opencv_java_bindings_generator=OFF \
                          -DPYTHON3_EXECUTABLE=/usr/bin/python3 \
                          -DOPENCV_GENERATE_PKGCONFIG=ON \
                          -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-%s/modules \
                          " % (get.installDIR(), get.srcVERSION()), sourceDir="..")
                          #  -DUSE_O3=OFF
                          #  -DUSE_OMIT_FRAME_POINTER=OFF


def build():
    shelltools.cd("build")
    #cmaketools.make()
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    # Move other docs and samples under standart doc dir
    #doc_dir = "usr/share/doc/" + get.srcNAME()

    #pisitools.domove("usr/share/opencv/doc", doc_dir)
    #pisitools.domove("usr/share/opencv/samples", doc_dir)
    
    shelltools.cd("..")

    pisitools.dodoc("README.md", "LICENSE", )

