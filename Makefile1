PKG="/Users/garen/dev/pyspeces/auto_test"
IMAGE?=github.com/wangkun/auto_test

docker-build:
    docker run -i --rm -v `pwd`:$(PKG) --workdir=/src

build-image: docker-build
	docker build -t $(IMAGE) .

.PHONY: docker-build build-image