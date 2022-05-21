all:
	python3 app.py

ui-build:ui-dev
	@echo "build UI static files."
	@cd ui && npm run build
	@mv ui/build/static/* static
	@mv ui/build/* templates

ui-start:ui-dev
	@echo "Start UI temporary server"
	@cd ui && npm start

ui-dev:
	@echo "Install UI requirements"
	@cd ui && npm install

clean:
	@echo "clean ui/node_modules"
	@cd ui && rm node_modules
