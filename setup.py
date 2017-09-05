from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

setup(
	name='nodel',
	version='0.2.4',
	packages=['nodel'],
	url='https://github.com/ary4n/nodel',
	license='MIT',
	author='aryan',
	author_email='alikhaniaryan@live.com',
	description='django project manager',
	keywords='minimal django project manager',
	download_url="https://github.com/ary4n/nodel/archive/0.2.4.tar.gz",
	install_requires=[
		'python-dotenv',
	],
)
