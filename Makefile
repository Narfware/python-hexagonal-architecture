#!/usr/bin/make -f
test-unit:
	pytest src/use_cases

test-component:
	pytest tests/component

