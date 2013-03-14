import os
import string

from fabric.api import *

def install(installdir, download_url, commands):
	if 'tar.gz' in download_url:
		suffix = 'tar.gz'
		unzip = 'tar zxf '
	elif 'zip' in download_url:
		suffix = 'zip'
		unzip = 'unzip '

	unzipdir = download_url.split('/')[-1][0:-(len(suffix)+1)]
	workdir = '%s-tmp' % installdir
	run('mkdir %s' % installdir)
	run('mkdir %s' % workdir)
	with cd(workdir):
		run('wget %s >/dev/null' % download_url)
		run('%s %s >/dev/null' % (unzip, download_url.split('/')[-1]))
		with cd(unzipdir):
			for command in commands:
				run(command)
	run('rm -rf %s' % workdir)
  
