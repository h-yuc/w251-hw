# Homework 11 -- More fun with OpenAI Gym!

## What parameters did you change? 
I change optimizer, number of layers, number of iterations, batch size, and threshold.

## What values did you try?

- optimizer: Adam, Adamax
- number of layers: (32, 32), (64, 64), (128, 64)
- number of iterations: 25000, 50000, 70000
- batch size: 16, 32, 64
- threshold: 1000, 3000, 5000

## Did you try any other changes that made things better or worse?
## Did they improve or degrade the model?

- Adamax optimizer made things better
- Add layer made things worse
- Increase number of iterations made things better
- Reduce batch size made things worse
- Reduce threshold made things better

## Based on what you observed, what conclusions can you draw about the different parameters and their values? 
Instead of adding more layers, increasing number of iterations and decreasing the threshold help to improve the total number of landings.

**Baseline:**

- optimizer: Adam
- number of layers: (32, 32)
- number of iterations: 50000
- batch size: 32
- threshold: 3000
- Total landings: 31
- Link: https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/first.mp4 

**Model 1:**

- optimizer: Adamax
- number of layers: (32, 32)
- number of iterations: 70000
- batch size: 32
- threshold: 1000
- Total landings: 82
- Link: https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/second.mp4

**Model 2:**

- optimizer: Adam
- number of layers: (128, 64)
- number of iterations: 25000
- batch size: 16
- threshold: 3000
- Total landings: 21
- Link: https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/third.mp4

**Model 3 (best model):**

- optimizer: Adamax
- number of layers: (32, 32)
- number of iterations: 70000
- batch size: 32
- threshold: 1000
- Total landings: 107
- Link: https://w251bucket-hw3.s3.us-east.cloud-object-storage.appdomain.cloud/fourth.mp4 