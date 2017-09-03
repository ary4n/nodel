import sys
import os

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


def call(params):
	os.system("python ./core/manage.py " + params)


def method_not_found(method):
	print("method not found: %s" % method)


from .functions import *

def run():
	args = sys.argv

	if len(args) > 1:
		method = args[1].split(':')

		if method[0] in functions:
			if len(method) > 1:
				if method[1] in functions[method[0]]:
					functions[method[0]][method[1]]['function'](args[2:], call)
				else:
					method_not_found(args[1])
			else:
				functions[method[0]]['default']['function'](args[2:], call)
		else:
			method_not_found(args[1])
