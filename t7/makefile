FUNCT = c
OUT ?= $(FUNCT)
MAXEVALS = 30
SIZE = 50
DIM = 2
OMEGA = 0.75
PHIP = 0.3
PHIG = 0.7
LR = 0.4
NBEST = 3

run:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 0 0 0

data:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 0 1 0

graphs:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 1 0 0

datagraphs:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 1 1 0

gif:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 0 0 1
	@ffmpeg -y -i ./figs/%02d.png ./figs/$(OUT).gif
	@rm figs/*.png
	@echo "Gif ${FUNCT}.gif created!"
	# @xdg-open ./figs/${FUNCT}.gif

datagif:
	@python3 ./src/main.py ./config.yaml $(FUNCT) $(MAXEVALS) $(SIZE) $(DIM) $(OMEGA) $(PHIP) $(PHIG) $(LR) $(NBEST) 0 1 1
	@ffmpeg -y -i ./figs/%02d.png ./figs/$(OUT).gif
	@rm figs/*.png
