# Project 8. Image Classification - Guess a Celebrity
Link: [Project-8.Computer_vision_image_classification.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-8/Project-8.Computer_vision_image_classification.ipynb)

The goal of the project is to train a neural network to classify images based on predefined classes. There are five classes representing celebrities from the tech space. The resulting model must classify new images based on these five classes. To do that we take a pretrained ResNet-34 model and apply different transfer learning strategies to train the model. We must reach the accuracy of above 85 % on the trained model.

The data volume in the training data set (3000 images) is rather small compared to the dataset used in the model training (> 1 million images) and the data in the training dataset is rather different from the one used in the pretraining. Thus I will apply one of the following strategies and pick the one showing the higher accuracy:
* Freeze the weights, replace the final dense layer, and update the weights only on the final dense layer.
* Freeze the weights, remove the last CNN layer, replace the final dense layer, and update the weights only on the final dense layer.
* Freeze the weights, remove the last two CNN layers, replace the final dense layer, and update the weights only on the final dense layer.

Removal of the last CNN layers is done because they contain the high level image information which is not applicable to the train dataset.

## Technology stack
Whily working on this project I have mastered:

* python
* pytorch
* torchvision
* matplotlib

## Conclusions
* 

## Figures
Random samples of train and validation images

![Random samples of train and validation images](https://i.imgur.com/fVMDsOy.jpg)
