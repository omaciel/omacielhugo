.PHONY: all install-hugo start-server dev setup

install-hugo:
	brew install hugo

setup:
	git submodule update --init --recursive

start-server: install-hugo
	hugo server -D

dev: install-hugo
	hugo serve -F

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "--- General Commands ---"
	@echo "setup				Initialize git submodules after cloning the repository."
	@echo "install-hugo			Install hugo on a MacOS system"
	@echo "start-server			Starts Hugo's development server to view the site."
	@echo "dev				Starts Hugo's development server with future posts enabled."
