# GeoAI_DL_group_3

This repository contains the code and dataset for **PV Panel Detection from High-Resolution Aerial Imagery in
Heidelberg using Deep Learning**.
Find our detailed paper [here](https://www.overleaf.com/project/671b97085108d3b868a1b10d).

## Usage

### 1. Training data
The original orthophoto was downloaded from [LGL-BW](https://opengeodata.lgl-bw.de/#/(sidenav:product/2)) and preprocessed. Then, it was manually labeled using Roboflow, split into three parts (train: 80%, val: 10%, test: 10%) and downloaded in the yolov11-format. The final training dataset can be found [here](https://github.com/MarenHeinemann/GeoAI_DL_group_3/data).


### 2. Training
The [training-folder](https://github.com/MarenHeinemann/GeoAI_DL_group_3/training) contains the python file used to train the model. 


### 3. Evaluation
The [evaluation-folder](https://github.com/MarenHeinemann/GeoAI_DL_group_3/evaluation) contains the python file used to evaluate the model.

## Results



# ToDo: Links (data), relative paths, figures, README