build:
	pip install wheel && python3 setup.py sdist bdist_wheel && pip install build && python3 -m build
publish:
	twine upload dist/*