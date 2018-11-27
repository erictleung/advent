## lint : Run Python code style checks
lint :
	pycodestyle -v advent201?/*

## test : Run unit tests
test :
	python -m unittest -v

## help : Help page for Makefile
help :
	@echo ""
	@echo "Usage:"
	@echo -e "\tmake <target>\n"
	@echo -e "Target\t\tDescription"
	@echo -e "------\t\t-----------"
	@grep '## [A-Za-z]* : [A-Za-z]*' $(MAKEFILE_LIST) | sed 's/## //' | sed 's/: /\t\t/'

.PHONY : test lint help

.DEFAULT_GOAL := help
