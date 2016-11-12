
help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	pip install -r requirements.txt
	python -m nltk.downloader punkt
	python -m nltk.downloader cmudict
	python setup.py install

tdd: ## Start a test runner with a watcher
	nodemon -e py -x sh -c "pytest -sx || true"

.PHONY: haikufinder/cmudict/cmudict.pickle
haikufinder/cmudict/cmudict.pickle:
	python haikufinder/cmudict/PickleCMUDict.py $@
