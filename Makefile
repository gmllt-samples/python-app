PORT ?= 8080

run:
	@echo "Starting server on port $(PORT)..."
	@PORT=$(PORT) python3 app.py

.PHONY: run
