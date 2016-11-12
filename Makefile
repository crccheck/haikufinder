
help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

tdd: ## Start a test runner with a watcher
	nodemon -e py -x sh -c "pytest -sx || true"
