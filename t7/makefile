FUNCT = c

run:
	@python3 ./src/main.py ./config.yaml $(FUNCT)

gif:
	@python3 ./src/main.py ./config.yaml $(FUNCT)
	@ffmpeg -y -i ./figs/%02d.png ./figs/$(FUNCT).gif
	@rm figs/*.png
