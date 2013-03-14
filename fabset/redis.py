import os
import string

from utils import *

def install_redis(installdir, download_url):
	install(installdir, download_url,
		['make PREFIX=%s install >/dev/null' % installdir,
		 'mkdir %s/conf' % installdir,
		 'cp redis.conf %s/conf' % installdir])

