from setuptools import setup, find_packages
import os

def description():
    path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(path) as readme:
        lines = []
        for line in readme:
            if line.startswith("Installation"): break
            lines.append(line)
        return "".join(lines).strip()

setup(name='terminal-colors',
	version='3.0.0',
	description='Utility to test color capabilities of terminal.',
	long_description=description(),
	author='John Eikenberry',
	author_email='jae@zhar.net',
    url="https://github.com/eikenb/terminal-colors",
    scripts=['terminal-colors'],
    packages=find_packages(),
	classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console :: Curses',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
