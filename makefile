CONTAINER = smrudptests
NAME = smrudptests1

.PHONY: run start attach stop rm

run:
	docker run --name $(NAME) -it --rm --privileged --pid='host' \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v '/home/gabriel/MEGA/Documentos/UFG/Projeto Ricardo/Testes/scripts/':/root/scripts \
	$(CONTAINER) \
	/bin/bash

start: 
	docker run --name $(NAME) -it --privileged --pid='host' \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v '/home/gabriel/MEGA/Documentos/UFG/Projeto Ricardo/Testes/scripts/':/root/scripts \
	$(CONTAINER) \
	/bin/bash

attach:
	docker container start $(NAME)
	docker container attach $(NAME)

stop:
	docker container stop $(NAME)

rm:
	docker container rm $(NAME)

default: run