build:
	docker build \
		--build-arg SMTP_USERNAME \
                --build-arg SMTP_PASSWORD \
                --build-arg RECEIVER_EMAIL \
                --build-arg SELLER_CENTRAL_ACCESS_KEY_ID \
                --build-arg SELLER_CENTRAL_SECRET_KEY \
                -t "anoti:dockerfile" .

run:
	docker run -it anoti:dockerfile /bin/bash
