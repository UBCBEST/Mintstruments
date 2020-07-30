test:
	python3 -m unittest

test-one:
	python3 -m unittest $(path)

typecheck:
	mypy --config-file mypy.ini src

typecheck-one:
	mypy --config-file mypy.ini $(path)

reformat:
	black .

prepush: reformat typecheck test
