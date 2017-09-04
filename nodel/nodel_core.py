import sys
import os
from dotenv import load_dotenv

from . import structure
functions = {}


def register(group=None, action=None, description=None):
	def decorator(view_func):
		if not group in functions:
			functions[group] = {}
		if action:
			functions[group][action] = {"description": description, "function": view_func}
		else:
			functions[group]['default'] = {"description": description, "function": view_func}
		return view_func

	return decorator


def django(params):
	os.system("python ./core/manage.py " + params)


def execute(command):
	os.system(command)


def method_not_found(method):
	print("method not found: %s" % method)




@register(group='run')
def run_server(params):
	os.nodel_core.django('runserver %s:%s' % (os.environ.get('ADDRESS', 'localhost'), os.environ.get('PORT', '8000')))


@register(group='run', action='service')
def run_service(params):
	execute('gunicorn --chdir %s --workers 10 --bind %s:%s core.wsgi:application' % (os.path.join(root_path(), 'core'), os.environ.get('ADDRESS', 'localhost'), os.environ.get('PORT', '8000')))


@register(group='make', action='service')
def make_service(params):
	name = os.path.basename(root_path())
	temp = os.path.join(os.path.abspath(os.environ.get('WORKON_HOME')), name)

	virtual_env_home = input('enter python home directory: (%s)' % temp)
	if not virtual_env_home:
		virtual_env_home = temp

	temp = os.environ.get('USER')
	user = input('enter user name: (%s)' % temp)
	if not user:
		user = temp

	temp = "10"
	workers = input('enter workers count: (%s)' % temp)
	if not workers:
		workers = temp

	with open(os.path.join(root_path(), '%s.service' % name), 'w') as f:
		f.write('[Unit]\n')
		f.write('Description=%s daemon\n' % name)
		f.write('After=network.target\n')
		f.write('[Service]\n')
		f.write('User=%s\n' % user)
		f.write('Group=www-data\n')
		f.write('WorkingDirectory=%s\n' % root_path())
		f.write('ExecStart=%(home)s/bin/gunicorn --access-logfile - --workers %(workers)s --bind unix:%(socket)s --chdir %(root)s core.wsgi:application\n' % {'home': virtual_env_home, 'root': root_path(), 'socket': os.path.join(root_path(), 'socket.sock'), 'workers': workers})
		f.write('[Install]\n')
		f.write('WantedBy=multi-user.target')


@register(group='make', action='project')
def make_project(params):
	version = input('Specify django project version (default is 1.11.3):')
	if not version:
		version = '1.11.3'
	version = version.replace('.', '_')

	django = getattr(structure, 'django_%s' % version, None)
	if django:
		django.make_project(root_path())
	else:
		print('no structure found for this version of django.')

	pass


@register(group='make', action='migrations')
def make_migrations(params):
	django('makemigrations')


@register(group='migrate')
def make_migrate(params):
	django('migrate')


@register(group='install')
def install(params):
	execute('python -m pip install -r modules/%s.txt' % os.environ.get('ENV', 'dev'))


def root_path():
	return os.path.dirname(os.path.abspath(sys.argv[0]))


def run():
	args = sys.argv

	dotenv_path = os.path.join(root_path(), '.env')
	load_dotenv(dotenv_path)

	if len(args) > 1:
		method = args[1].split(':')

		if method[0] in functions:
			if len(method) > 1:
				if method[1] in functions[method[0]]:
					functions[method[0]][method[1]]['function'](args[2:])
				else:
					method_not_found(args[1])
			else:
				functions[method[0]]['default']['function'](args[2:])
		else:
			method_not_found(args[1])
