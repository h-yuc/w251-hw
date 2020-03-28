# Homework 5

### Questions:

1. What is TensorFlow? Which company is the leading contributor to TensorFlow?

**TensorFlow is a Python-friendly open source library for numerical computation that makes machine learning faster and easier. Google has built up copious quantities of goodwill with developers for its contributions of TensorFlow.**

2. What is TensorRT? How is it different from TensorFlow?

**NVIDIA TensorRT is an SDK for high-performance deep learning inference. It includes a deep learning inference optimizer and runtime that delivers low latency and high-throughput for deep learning inference applications. TensorFlow Serving is a flexible, high-performance serving system for machine learning models, NVIDIA TensorRT is a platform for high-performance deep learning inference, and by combining the two, users can get better performance for GPU inference in a simple way.**

3. What is ImageNet? How many images does it contain? How many classes?

**The ImageNet is a large visual database designed for use in visual object recognition software research. More than 14 million images have been hand-annotated by the project to indicate what objects are pictured and in at least one million of the images, bounding boxes are also provided. ImageNet contains more than 20,000 classes.**

4. Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.

**The difference between MobileNet and GoogleNet (Inception) architectures is that, MobileNet forms a factorized convolutions which simplified a standard convolution into a depthwise separable convolution. GoogleNet is based on Inception architecture which expands the network to achieve high performance and high computation efficiency.**

5. In your own words, what is a bottleneck?

**A bottleneck is the input layer below the final output layer in a fully-connected neural network and it provides a compact representation of the network.**

6. How is a bottleneck different from the concept of layer freezing?

**Layer freezing freezes the weights of a pre-trained model, so the layer does not get updated in the training. Bottleneck identifies a compact layer and caches the earlier layers. Bottleneck is similar that it applys layer freezing to all layers except last layer. Bottleneck layer reduces the dimensionality of the input during transfer learning.**

7. In this lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)

**This lab uses cached results and downloads the previous layers directly. The previous layers came from a pre-trained model and they are used to calculated the bottlenecks for every image.**

8. How does a low `--learning_rate` (step 7) value (like 0.005) affect the precision? How much longer does training take?

**A low learning rate (0.005) increases the training time by ~5 mins, the precision increased to 91.4% from 88% (default=0.1).**

9. How about a `--learning_rate` (step 7) of 1.0? Is the precision still good enough to produce a usable graph?

**A learning rate of 1.0 takes about the same time as default. The precision has a wide range of accuracies, but mostly around 90%. The precision is still good enough to produce a usable graph.**

10. For step 8, you can use any images you like. Pictures of food, people, or animals work well. You can even use [ImageNet](http://www.image-net.org/) images. How accurate was your model? Were you able to train it using a few images, or did you need a lot?

**I use images of cats (http://www.image-net.org/search?q=cat). My model accuracy was 72.37% with learning rate 0.1. I was able to train it using a few images.** 

11. Run the script on the CPU (see instructions above) How does the training time compare to the default network training (section 4)?  Why?

**The training time on CPU was takes longer (~ 13 mins) compare to the default network training. It is because TensorRT is optimized by Nvidia CUDA based GPU.**

12. Try the training again, but this time do `export ARCHITECTURE="inception_v3"` Are CPU and GPU training times different?

**Yes, CPU training time is shorter. CPU training time: 1013.842 seconds. GPU training time: 1323.217 seconds.**

13. Given the hints under the notes section, if we trained Inception_v3, what do we need to pass to replace ??? below to the label_image script?  Can we also glean the answer from examining TensorBoard?
```
python -m scripts.label_image --input_layer=299 --input_height=299 --input_width=299  --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```
**We need to pass 299 to replace ???.**

### To turn in:
Turn in a text file or pdf with your answers to the questions above.
Please note that this homework is NOT graded, credit / nocredit only.
