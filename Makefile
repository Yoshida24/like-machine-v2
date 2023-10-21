.PHONY: setup
setup:
	@echo "Setup..."
	sh scripts/setup.sh

.PHONY: run
run:
	@echo "Running..."
	sh scripts/run.sh

.PHONY: serve
serve:
	@echo "Serving..."
	sh scripts/serve.sh

.PHONY: test
test:
	@echo "Testing..."
	sh scripts/test.sh
