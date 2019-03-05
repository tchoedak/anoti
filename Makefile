build:
	docker build \
		--build-arg SMTP_USERNAME \
                --build-arg SMTP_PASSWORD \
                --build-arg SELLER_CENTRAL_ACCESS_KEY_ID \
                --build-arg SELLER_CENTRAL_SECRET_KEY \
		--build-arg ACCOUNT_SID \
		--build-arg AUTH_TOKEN \
		--build-arg ANOTI_NUMBER \
                -t "anoti:dockerfile" .

run:
	docker run --name ${SELLER} -it -d anoti:dockerfile /bin/bash

connect:
	docker exec -it ${SELLER} /bin/bash

stop:
	docker stop ${SELLER}
