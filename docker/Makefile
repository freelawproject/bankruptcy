# Run with make push --file docker/Makefile
# Note that makefiles differentiate between tabs and spaces in a weird way!

DOCKER_REPOSITORY ?= freelawproject/bankruptcy-extractor

DOCKER ?= docker
export DOCKER

DOCKER_TAG = $(shell head -1 docker/version.txt)

.PHONY: all image push multiarch_push multiarch_image

UNAME := $(shell uname -m)

all: image

image:
	$(DOCKER) build -t $(DOCKER_REPOSITORY):$(DOCKER_TAG) -t $(DOCKER_REPOSITORY):latest --file docker/Dockerfile .

push: image
	$(info Checking if valid architecture)
	@if [ $(UNAME) = "x86_64" ]; then \
		echo "Architecture is OK. Pushing.";\
		$(DOCKER) push $(DOCKER_REPOSITORY):$(DOCKER_TAG);\
        $(DOCKER) push $(DOCKER_REPOSITORY):latest;\
	else \
		echo "Only arm64 machines can push single-architecture builds. If you want to \
push a build, try 'make multiarch_push', which builds for both arm64 and amd64. This \
protects against arm64 builds being accidentally deployed to the server (which uses arm64).";\
	fi

multiarch_image:
	export DOCKER_CLI_EXPERIMENTAL=enabled
	$(DOCKER) buildx rm
	$(DOCKER) buildx create --use --name flp-builder
	$(DOCKER) buildx build --platform linux/amd64,linux/arm64 -t $(DOCKER_REPOSITORY):latest -t $(DOCKER_REPOSITORY):$(DOCKER_TAG) --file docker/Dockerfile .

multiarch_push: multiarch_image
	$(DOCKER) buildx build --push --platform linux/amd64,linux/arm64 -t $(DOCKER_REPOSITORY):latest -t $(DOCKER_REPOSITORY):$(DOCKER_TAG) --file docker/Dockerfile .

x86_push:
	export DOCKER_CLI_EXPERIMENTAL=enabled
	$(DOCKER) buildx rm
	$(DOCKER) buildx create --use --name flp-builder
	$(DOCKER) buildx build --push --platform linux/amd64 -t $(DOCKER_REPOSITORY):latest -t $(DOCKER_REPOSITORY):$(DOCKER_TAG) --file docker/Dockerfile .
