repo=aidonode-dummy_image_source
# repo=$(shell basename -s .git `git config --get remote.origin.url`)
branch=$(shell git rev-parse --abbrev-ref HEAD)
tag=duckietown/$(repo):$(branch)

build:
	docker build -t $(tag) .

build-no-cache:
	docker build -t $(tag)  --no-cache .

push: build
	docker push $(tag)


test-data1-direct:
	./dummy_image_source.py < test_data/in1.json > test_data/out1.json

test-data1-docker:
	docker run -i $(tag) < test_data/in1.json > test_data/out1.json

test-describe:
	./dummy_image_source.py < test_data/describe.json

#
#protocols=/data/work/vmware-michela-shared/DT/dt-env/dt-env-developer/src/aido-protocols
#
#other=-v $(protocols):/src/aido-protocols/
#other=
