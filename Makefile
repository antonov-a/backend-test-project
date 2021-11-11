VENV_PATH=.venv

.PHONY:virtualenv test run seed clean

virtualenv:
	virtualenv "${VENV_PATH}"
	"${VENV_PATH}/bin/pip" install -r pip-requirements.txt

test:
	./.venv/bin/pytest -v

run:
	./.venv/bin/python3 src/app.py

seed:
	./.venv/bin/python3 populate_db.py

clean:
	rm -rf .venv
	rm -rf products.sqlite
