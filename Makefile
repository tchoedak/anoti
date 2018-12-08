build:
	docker build \
		--build-arg SMTP_USERNAME \
                --build-arg SMTP_PASSWORD \
                --build-arg RECEIVER_EMAIL \
                --build-arg SELLER_CENTRAL_ACCESS_KEY_ID \
                --build-arg SELLER_CENTRAL_SECRET_KEY \
		--build-arg ACCOUNT_SID \
		--build-arg AUTH_TOKEN \
		--build-arg RECEIVER_NUMBER \
		--build-arg ANOTI_NUMBER \
                -t "anoti:dockerfile" .

run:
	docker run -it -d anoti:dockerfile /bin/bash

connect:
	docker exec -it `docker ps --format "{{.Names}}"` /bin/bash

stop:
	docker stop `docker ps --format "{{.Names}}"`
