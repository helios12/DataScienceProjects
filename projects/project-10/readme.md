# Project 10. Segmentation of space objects
Link: [Project-10.Satellites_segmentation.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-10/Project-10.Satellites_segmentation.ipynb)

The goal of the project is to pick and train an image segmentation model on a dataset of satelite images. The dataset contains images of satelites and image masks with segments referring to parts of the satelite like the body, solar panel and antenna, marked, respectively, with three colors - green, red and blue.
Train model must segment arbitrary satelite images with the mIoU value of above 0.7. Inference results of the trained model must be visualized.

## Technology stack
Whily working on this project I have mastered:

* python
* pytorch
* torchvision
* matplotlib
* DeepLabV3 with a ResNet-50 backbone


## Conclusions
The trained model has achieved the mIoU value of 0.71 on the validatation dataset, which is above the target defined for this project.

Inference examples visually confirm a good level of segmentation.


## Figures
Satelite image segmentation 1

![Satelite image segmentation 1](https://i.imgur.com/3zOdflE.png)

Satelite image segmentation 2

![Satelite image segmentation 2](https://i.imgur.com/E4K3ndh.png)

Satelite image segmentation 3

![Satelite image segmentation 3](https://i.imgur.com/pz0kfg2.png)

Satelite image segmentation 4

![Satelite image segmentation 4](https://i.imgur.com/4GD2xPo.png)
