build:
	docker build -t "anoti:dockerfile" .

run:
	docker run -it anoti:dockerfile /bin/bash

