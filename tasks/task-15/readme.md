# Task-15. Image Captioning
Link: [Task-15-Image_Captioning.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-15/Task-15-Image_Captioning.ipynb)

The goal of the task is to generate captions to an image. To do that we will use a hybrid architecture linking CNN and LSTM. By varying the embedding size and the number of epochs we need to empirically check whether the quality of captions generation can be improved. Models will be trained on the `Flickr8k` dataset.

## Technology Stack
While working on this task I have mastered:

* python
* pytorch
* Encoder / decoder architecture with Inception V3 and LSTM
* Matplotlib

## Conclusions
I was alble to train the model and get consistently better results by increasing the embedding size and number of epochs.

## Figures

Image caption with embedding size 1024 and 10 epochs of training.

![Image caption with embedding size 1024 and 10 epochs of training](https://i.imgur.com/HAR30su.png)

Image caption with embedding size 512 and 10 epochs of training.

![Image caption with embedding size 512 and 10 epochs of training](https://i.imgur.com/0ha6hCL.png)
