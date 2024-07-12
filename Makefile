install: #инсталяция
	poetry install
brain-games: #запуск?
	poetry run brain-games
build: #собрать какой то пакет
	poerty build
publish: #хз че это
	poetry publish --dry-run
package-install: #инсталяция чего то
	python3 -m pip install --user dist/*.whl
