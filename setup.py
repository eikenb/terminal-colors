from setuptools import setup

setup(name='terminal-colors',
	version='2.3',
	description='Utility to test color capabilities of terminal.',
	long_description=open('README.md').read(),
	author='John Eikenberry',
	author_email='jae@zhar.net',
    url="https://github.com/eikenb/terminal-colors",
    scripts=['terminal-colors'],
	classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console :: Curses',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
