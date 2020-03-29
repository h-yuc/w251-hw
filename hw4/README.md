# Homework 4: DL 101

#### 2. ConvnetJS MNIST demo
In this lab, we will look at the processing of the MNIST data set using ConvnetJS.  This demo uses this page: http://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html
The MNIST data set consists of 28x28 black and white images of hand written digits and the goal is to correctly classify them.  Once you load the page, the network starts running and you can see the loss and predictions change in real time.  Try the following:

* Name all the layers in the network, make sure you understand what they do.

 **- input layer: this is the initial layer with input training image (24 x 24).**
 
 **- convolutional layer: this layer extracts features from images and it has 8 (5 x 5) kernels which strides through the input image with 1 pixel and creates 2 pixels wide pad around each image. The activate function is relu.**
 
 **- pool layer: this layer helps reduce the spatial complexity and have filter size 2 x 2 with stride = 2.**
 
 **- output layer: the fully-connected layer uses a softmax function to predict the output classes with probabilities(there are 10 classes).**

* Experiment with the number and size of filters in each layer.  Does it improve the accuracy?

 **Increasing the size of the filter improve the accuracy but make the difference in accuracy larger between training and validation set. Reducing the size of filter improves the accuray.**

* Remove the pooling layers.  Does it impact the accuracy?

 **Removing the pooling layer will reduce the accuracy.**

* Add one more conv layer.  Does it help with accuracy?

 **Adding one more conv layer will improve the accuracy but make the difference in accuracy larger between training and validation set.**

* Increase the batch size.  What impact does it have?

 **Increasing the batch size will make the training time slower and the gradient become smaller, which slow down the reduction of loss.**

* What is the best accuracy you can achieve? Are you over 99%? 99.5%?

 **The best validation accuray I can achieve is 99%.**

#### Submission:
Please submit answers to #2, and a html download of your completed Jupyter notebook.   
Please mail these to your instructors. 
