download-old-year:
	python init.py --year ${ARGS}

download-today:
	python init.py --today

check-files:
	pre-commit run --all-files