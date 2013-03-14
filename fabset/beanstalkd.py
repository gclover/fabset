import os
import string

from utils import *

def install_beanstalkd(installdir, download_url):
	install(installdir, download_url,
		['make install PREFIX=%s >/dev/null' % installdir])

