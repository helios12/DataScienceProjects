# Project 11. Image Style Transfer
Link: [Project-11.Image_style_transfer_model.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-11/Project-11.Image_style_transfer_model.ipynb)

The goal of the project is to implement an image style transfer algorithm and then be able to apply the trained model in a different application to an arbitrary image. The style is defined by a collection of 268 paintings of Van Gogh. The model is a feed-forward convolutional neural network that transforms a content image into a stylized version. A pretrained VGG19 network is used for feature extraction. A python console application has been developed to apply the style to an arbitrary image.

## Technology stack
Whily working on this project I have mastered:

* python
* pytorch
* torchvision
* matplotlib

## Conclusions
The trained model is consistently applying style to arbitrary images. Though the color palette of the images is quite limited.

## Figures
Cats image - no style

![Cats image - no style](https://i.imgur.com/mNL8LO6.jpg)

Cats image - transferred style

![Cats image - transferred style](https://i.imgur.com/zLpLIWr.jpg)

London image - no style

![London image - no style](https://i.imgur.com/NZyvsBC.jpg)

London image - transferred style

![London image - transferred style](https://i.imgur.com/9IjzIxl.jpg)

Paris image - no style

![Paris image - no style](https://i.imgur.com/llpRzIw.jpg)

Paris image - transferred style

![Paris image - transferred style](https://i.imgur.com/IwjFNCV.jpg)
