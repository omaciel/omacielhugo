.PHONY: all install-hugo start-server

install-hugo:
	brew install hugo

start-server:
	hugo server -D

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "--- General Commands ---"
	@echo "install-hugo			Install hugo on a MacOS system"
	@echo "start-server			Starts Hugo’s development server to view the site."