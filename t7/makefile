FUNCT = c
OUT ?= $(FUNCT)

run:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 0 0 0

data:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 0 1 0

graphs:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 1 0 0

datagraphs:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 1 1 0

gif:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 0 0 1
	@ffmpeg -y -i ./figs/%02d.png ./figs/$(OUT).gif
	@rm figs/*.png

datagif:
	@python3 ./src/main.py ./config.yaml $(FUNCT) 0 1 1
	@ffmpeg -y -i ./figs/%02d.png ./figs/$(OUT).gif
	@rm figs/*.png
