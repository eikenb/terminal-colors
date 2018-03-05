# help me remember 'python setup' commands

help:
	pypi - build sdist/bdist_egg and upload to pypi
	clean - remove pypi leftovers

pypi:
	python3 setup.py sdist bdist_egg upload

clean:
	rm -rf build dist terminal_colors.egg-info

