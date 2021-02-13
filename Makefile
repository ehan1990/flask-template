PORT=5050

run:
	python3 app.py

health:
	@curl localhost:${PORT}/healthcheck

# VAL=5 make post
post:
	@curl localhost:${PORT}/example -X POST -H "Content-Type: application/json" -d '{"val": ${VAL}}'

list:
	@curl localhost:${PORT}/example

build:
	docker-compose build

run-container:
	docker-compose up --build

ssh-container:
	docker exec -it flask-template-container /bin/bash

down:
	docker-compose down