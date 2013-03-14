
from fabric.api import *
from openresty import *
from redis import *

env.hosts = ['localhost']
env.user = 'elan'
env.password = ''

def test_install_openresty():
	install_openresty('/opt/space/test2', 'http://agentzh.org/misc/nginx/ngx_openresty-1.2.4.14.tar.gz')

def test_install_redis():
	install_redis('/opt/space/test9', 'http://redis.googlecode.com/files/redis-2.6.9.tar.gz')

def test_install_beanstalkd():
	install_redis('/opt/space/test10', 'http://cloud.github.com/downloads/kr/beanstalkd/beanstalkd-1.8.tar.gz')


