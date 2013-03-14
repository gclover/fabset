import os
import string

from utils import *

def install_openresty(installdir, download_url):
	install(installdir, download_url,
		['./configure --with-luajit --prefix=%s >/dev/null' % installdir, 
		 'make >/dev/null', 'make install >/dev/null'])

