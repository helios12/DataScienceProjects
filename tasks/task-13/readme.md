# Task-13. Practise Segmentation
Link: [Task-13-Segmentation_practice.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-13/Task-13-Segmentation_practice.ipynb)

The goal of the task is to train a segmentation model. Using the Oxford-IIIT Pet Dataset an image segmentation model should be trained. The dataset contains the masks. On the validation step the IoU metric value of at least 0.7 must be achieved.

## Technology Stack
While working on this task I have mastered:

* python
* pytorch
* DeepLabV3-ResNet50
* Matplotlib

## Conclusions
I was able to prepare a dataset with data augmentations via `albumentations` library and a dataloader on top of it. After that a DeepLabV3-ResNet50 model has been trained for 20 epochs. The IoU metric value achieved in the validation was 0.918.

## Figures

Training images and their masks after applying augmentations
![Training images and their masks after applying augmentations](https://i.imgur.com/kl8bKjr.png)
