.PHONY: all lint test test-cov install dev clean distclean

PYTHON ?= python

all: ;

lint:
	flake8

test: all
	py.test

test-cov: all
	py.test --cov=q2_dynamo

install:
	$(PYTHON) setup.py install

dev: all
	pip install -e .

clean: distclean

distclean: ;