# Project 12. Final Project: Development of a Virtual Fitness Trainer
Link: [Project-12.Development_of_a_virtual_fitness_trainer.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-12-final/Project-12.Development_of_a_virtual_fitness_trainer.ipynb)

This project develops a video-based human movement similarity evaluation system intended for use in an automated fitness trainer. The system analyzes a reference exercise video and a user-recorded performance by extracting human body keypoints using a deep-learning-based pose estimation model. The extracted pose sequences are normalized and compared using confidence-weighted similarity metrics, while Dynamic Time Warping (DTW) is employed to align movements performed at different speeds. The implementation is developed in Python using PyTorch, Torchvision, OpenCV, NumPy, and DTW-based sequence alignment techniques.

The similarity evaluation pipline consists of the following steps:
* Extract video frames from the reference and user-recorded exercise videos using OpenCV.
* Detect human body keypoints in each frame using the pre-trained Keypoint R-CNN model from Torchvision.
* Convert detected keypoints into pose representations and associate them with confidence scores.
* Normalize poses to reduce the influence of subject position and body scale differences.
* Compute pairwise pose distances between all frames of the two videos using confidence-weighted similarity metrics.
* Construct a frame-to-frame cost matrix representing pose dissimilarity across the two sequences.
* Apply Dynamic Time Warping (DTW) to temporally align movements performed at different speeds.
* Aggregate the distances of aligned poses to obtain an overall movement similarity score.
* Use the resulting similarity metrics to evaluate how closely the user's exercise matches the reference movement.

## Technology stack
Whily working on this project I have mastered:

* python
* pytorch
* torchvision
* OpenCV

## Conclusions
This project successfully demonstrates a pipeline for evaluating the similarity of human movements from video recordings. By combining pose estimation, pose normalization, confidence-weighted similarity metrics, and Dynamic Time Warping, the system can compare exercises performed at different speeds and provide an objective similarity score. Validation experiments showed that the pipeline reliably distinguishes between identical and reproduced movements while maintaining high alignment accuracy. The developed approach provides a practical foundation for future fitness coaching applications capable of automatically assessing exercise performance from video.

## Figures
Keypointed image 1 (video frame)

![Keypointed image 1 (video frame)](https://i.imgur.com/CwuEUDg.png)

Keypointed image 2 (video frame)

![Keypointed image 2 (video frame)](https://i.imgur.com/PKMWdDi.png)

Keypointed image 3 (video frame)

![Keypointed image 3 (video frame)](https://i.imgur.com/cGhEROG.png)

## Videos
**Original videos**

* Reference video: https://github.com/helios12/DataScienceProjects/blob/main/projects/project-12-final/data/yoga_girl.mp4
* Sample video: https://github.com/helios12/DataScienceProjects/blob/main/projects/project-12-final/data/yoga_me.mp4


**Keypointed videos**
* Reference video: https://github.com/helios12/DataScienceProjects/blob/main/projects/project-12-final/data/input_keypoints_output_4389c312.mp4
* Sample video: https://github.com/helios12/DataScienceProjects/blob/main/projects/project-12-final/data/sample_positive_keypoints_output_47e073bb.mp4