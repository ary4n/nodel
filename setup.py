from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

setup(
	name='nodel',
	version='0.1.2',
	packages=['nodel'],
	url='https://github.com/ary4n/nodel',
	license='MIT',
	author='aryan',
	author_email='alikhaniaryan@live.com',
	description='django project manager',
	keywords='minimal django project manager',
	install_requires=[
		'python-dotenv',
	],
)
