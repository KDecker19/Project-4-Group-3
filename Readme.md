About the Project:

This is a repository using a neural network to recognize images of dogs, and identify and classify the breed.  The model was trained on image data from a dog image dataset found at https://www.kaggle.com/datasets/miljan/stanford-dogs-dataset-traintest.  This is a modified version of the Stanford dogs dataset found at http://vision.stanford.edu/aditya86/ImageNetDogs/ which uses images and annotation from ImageNet for image categorization.


Project Collaborators:

Kaleb Decker
Dena Wetmore
Steven Anthony
Jack Ritz
Em Needles

Contents of the dataset:
Number of categories: 120 dog breeds
Number of images: 9,600 dog images


Contents of the repository:

Data folder
Resources folder - with a test folder & train folder containing folders for images of each dog breed

Visual folder - app_vis.js, vis.html, breed-options.php, breed-info.php

DataBase Testing.ipynb



Test.ipynb

Screenshot 2024-03-07 205735.png

Project_4

Project_4 folder
Project_4_Machine_Learning.ipynb
SQLconnection3.ipynb
dog_model.h5
Dog_model_2.h5
dogs.db
image_classification.ipynb


gitignore

Readme





Pre-processing:

Database Testing.ipynb connects to our SQLite database and imports the dog images with their correct breed labels.

SQLConnection3.ipynb

dogs.db  

The test.ipynb file formats the folder names for the dog breed categories, using a for loop, to remove hyphens.

Training:

Model trained on 9600 images
In test.ipynb a data generator was created and the dog images were loaded to memory.  The VGG16 model was then loaded, with some layers being unfrozen and a fully connected layer was added.  The model was then compiled with a smaller learning rate and the model was trained with more epochs.

test.ipynb file



Model fitting  

Testing:

Image upload

Visual folder - app_vis.js, vis.html, breed-options.php, breed-info.php > dog breed selector


Model Optimization




References for the Original Dataset:

Primary:
Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011. [pdf] [poster] [BibTex]
Secondary:
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li and L. Fei-Fei, ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and Pattern Recognition (CVPR), 2009. [pdf] [BibTex]
