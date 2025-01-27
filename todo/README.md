## TODO
* [ ] Add data to data/raw
* [ ] Add normalized and processed data to data/processed
* [ ] Create model and put it into models
* [ ] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
* [ ] Add a model file and a training script and get that running
* [ ] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
* [ ] Do a bit of code typing and remember to document essential parts of your code
* [ ] Setup version control for your data or part of your data
* [ ] Construct one or multiple docker files for your code
* [ ] Build the docker files locally and make sure they work as intended
* [ ] Write one or multiple configurations files for your experiments
* [ ] Used Hydra to load the configurations and manage your hyperparameters
* [ ] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [ ] Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,
      consider running a hyperparameter optimization sweep.
* [ ] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### COMMAND PROMPT
- 'git clone https://github.com/malek-luky/Automatic-Wheel-Assembly-Detection.git'
- docker build -f dockerfiles/Dockerfile . -t setup:latest (dont forget the dot)
- docker run --name setup -v %cd%/models:/models/ setup:latest
- docker run --name setup setup:latest
- docker run --name mlops -it --entrypoint sh setup:latest

### DOCKER
- start docker?
- conda create -n ml_ops python=3.10.9
- conda activate ml_ops
- python -m pip install --upgrade pip???
- 'pip install -r requirements.txt'
- 'dvc pull'

### MAKEFILE
- 'python src/data/make_dataset.py'
- 'python train_model.py'... (might be replaces by docker entrypoint?)
