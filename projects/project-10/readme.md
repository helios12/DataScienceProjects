# Project 9. Detection of medical masks
Link: [Project-10.Satellites_segmentation.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-10/Project-10.Satellites_segmentation.ipynb)

The goal of the project is to pick and train an image segmentation model on a dataset of satelite images. The dataset contains images of satelites and image masks with segments referring to parts of the satelite like the body, solar panel and antenna, marked, respectively, with three colors - green, red and blue.

!!!Continue here.

The goal of the project is to train two image detection models (RCNN and YOLO) on a dataset of images containing people wearing medical masks. The resulting model must detect images of people wearing medical masks, wearing them incorrectly or not wearing a medical mask. The data is labeled for the consumption by the RCNN model. Preparing labels for consumption by YOLO is also a part of the task. The minimum target mAP metric for both of the models is 0.85.

The training time of both models must be recorded and compared. Assuming the achieved mAP metric of both models is the same, the training time will be the deciding factor of the model performance.

## Technology stack
Whily working on this project I have mastered:

* python
* pytorch
* torchvision
* matplotlib
* Faster RCNN
* YOLO v5

## Conclusions
The Faster RCNN model has reached the `mAP_50`value of 0.86 after 20 epochs and 8.96 hours of training.
The YOLO 5m model has reached  the `mAP_50`value of 0.85 after 20 epochs and 1.3 hours of training.

So, the achieved metric value is very close. As expected the YOLO model has shown a better training time with a factor of around 7. Which is close to the expected 10-fold difference in training time between Faster RCNN and YOLO 5. Also taking into account the YOLO model setup simplicity, I would personally prefer it for usage in my projects.


## Figures
RCNN labels 1

![RCNN labels 1](https://i.imgur.com/ptgAfXq.png)

RCNN predicions 1

![RCNN predicions 1](https://i.imgur.com/fkBHMSv.png)

RCNN labels 2

![RCNN labels 2](https://i.imgur.com/57tBJt0.png)

RCNN predicions 2

![RCNN predicions 2](https://i.imgur.com/8G3NJYz.png)

YOLO labels 1

![YOLO labels 1](https://i.imgur.com/9PAqQeJ.jpg)

YOLO predicions 1

![YOLO predicions 1](https://i.imgur.com/crxoJee.jpg)

