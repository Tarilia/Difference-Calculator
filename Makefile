install: # установка пакета после клонирования репозитория или удаления зависимостей
	poetry install

build: # сборка пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: # установка пакета в систему
	python3 -m pip install --user dist/*.whl

lint: # запуск линтера
	poetry run flake8 gendiff

package-reinstall: # переустановка пакета в систему после обновления
	pip install --user --force-reinstall dist/*.whl
