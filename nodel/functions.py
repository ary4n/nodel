from . import nodel_core
from os import environ


@nodel_core.register(group='run')
def run_server(params, call):
	call('runserver %s:%s' % (environ.get('ADDRESS', 'localhost'), environ.get('PORT', '8000')))


@nodel_core.register(group='make', action='migrations')
def make_migrations(params, call):
	call('makemigrations')


@nodel_core.register(group='make', action='migrate')
def make_migrate(params, call):
	call('migrate')
