from . import nodel
from os import environ


@nodel.register(group='run')
def run_server(params, call):
	call('runserver %s:%s' % (environ.get('ADDRESS', 'localhost'), environ.get('PORT', '8000')))


@nodel.register(group='make', action='migrations')
def make_migrations(params, call):
	call('makemigrations')


@nodel.register(group='make', action='migrate')
def make_migrate(params, call):
	call('migrate')
