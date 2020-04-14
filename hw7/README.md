# Homework 7 - Neural face detection pipeline

### Questions
* Describe your solution in detail.  What neural network did you use? What dataset was it trained on? What accuracy does it achieve?

**I used a mobilenet SSD, which is a single shot multibox detector based face detector. It trained on the WIDERFACE dataset with accuracy around 85%.**

* Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?

**Yes, it achieved reasonable accuracy in my empirical tests. I would use this to develop a robust production-grade system.**

* What framerate does this method achieve on the Jetson? Where is the bottleneck?

**The framerate is around 11 fps. The bottleneck is the speed.**

* Which is a better quality detector: the OpenCV or yours?

**OpenCV is a better quality detector as it's faster and very low false positve rate.**

Images:
https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/img1214.png
https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/img1223.png
https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/img1228.png
https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/img1237.png