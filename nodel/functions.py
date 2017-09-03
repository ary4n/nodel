from . import nodel_core
from os import environ
import os

HERE = os.path.dirname(os.path.abspath(__file__))


@nodel_core.register(group='run')
def run_server(params):
	nodel_core.django('runserver %s:%s' % (environ.get('ADDRESS', 'localhost'), environ.get('PORT', '8000')))


@nodel_core.register(group='make', action='project')
def make_project(params):
	version = raw_input('Specify django project version (default is 1.11.3):')
	print(version)
	pass


@nodel_core.register(group='make', action='migrations')
def make_migrations(params):
	nodel_core.django('makemigrations')


@nodel_core.register(group='make', action='migrate')
def make_migrate(params):
	nodel_core.django('migrate')
