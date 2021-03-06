PORT=5050

dev-setup:
	pip3.8 install -r requirements-dev.txt

test:
	pytest -v --junitxml testreport.xml

run:
	python3 app.py

health:
	@curl localhost:${PORT}/healthcheck

# VAL=5 make post
post:
	@curl localhost:${PORT}/example -X POST -H "Content-Type: application/json" -d '{"val": ${VAL}}'

list:
	@curl localhost:${PORT}/example

cicd-build:
	docker build -t flask-template:latest .

build:
	docker-compose build

run-container:
	docker-compose up --build

ssh-container:
	docker exec -it flask-template-container /bin/bash

down:
	docker-compose down