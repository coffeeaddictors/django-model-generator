runserver:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

mm:
	make makemigrations

migrate:
	python3 manage.py migrate

m:
	make migrate

init:
	./entrypoint.sh
