from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant filex
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='nodel',
	version='0.1.0',
	packages=['nodel'],
	url='https://github.com/ary4n/nodel',
	license='MIT',
	author='aryan',
	author_email='alikhaniaryan@live.com',
	description='django project manager',
	long_description=long_description,
	keywords='minimal django project manager',
	download_url='https://github.com/ary4n/nodel/archive/0.1.0.tar.gz',
	install_requires=[
		'python-dotenv',
	],
)
