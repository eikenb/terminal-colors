# help me remember 'python setup' commands

help:
	pypi - build sdist/bdist_egg and upload to pypi
	clean - remove pypi leftovers

pypi:
	python3 setup.py sdist bdist_egg upload

release:
	@echo git tag -a vX.XX.X -s -f
	@echo git push --tags
	@echo
	@echo Then follow instructions here to GPG sign it for Debian.
	@echo https://wiki.debian.org/Creating%20signed%20GitHub%20releases

clean:
	rm -rf build dist terminal_colors.egg-info

