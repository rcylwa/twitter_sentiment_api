# Twitter US Airline Sentiment Classification REST API

Example project describing how to build a REST API that classifies sentiment in US Airline twitts.
The proposed solution uses:
* [fast.ai](https://github.com/fastai/fastai) high-level wrapper of pytorch library for building and exporting my model
* flask for wrapping a model in a REST API
* Docker for contenerization of the API
* Kubernetes cluster on Google Cloud Platform for an example deployment

Description of the dataset can be found here: [Twitter US Airline Sentiment](https://www.kaggle.com/crowdflower/twitter-airline-sentiment/home)

And downloaded using Kaggle API:
```shell
kaggle datasets download -d crowdflower/twitter-airline-sentiment
```

Conda environement used for developement of thos project cen be recreated using:
```shell
conda env create -f environment.yml
conda activate myenv
```

# Model building
For this part I used n1-highmem-8 VM on Google Cloud Platform.

All notebooks for training, evaluating and saving the model can be found in **nbs/**.

Sentiment classifier is build using pre-trained models from the fastai.text module.
I followed the example of IMDB sentiment classifier build using 
[ULMFiT](https://docs.fast.ai/text.html#Quick-Start:-Training-an-IMDb-sentiment-model-with-ULMFiT)


This approach is based on fine-tuning existing pre-trained models and is supposed to deliver state-of-the-art 
performance in sentiment analysis.

Few lines of code led to 83% test set accuracy.

# Deployment

To serve a model a simple **app/rest_api.py** flask app is provided.
This defines an endpoint that takes a single input (not a batch) and runs on CPU leading to an inexpensive and scalable solution.

Docker image with this app can be found on DockerHub: rcylwa/sentiment_api

Necessary Dockerfile for building an image yourself is also provided.

I created a Kubernetes cluster on my VM and run my docker image for DockerHub:

![](screenshots/scrn1.png?raw=true)

Verify that my pod is running:

![](screenshots/scrn2.png?raw=true)

Expose my pod on port 80 to the outside world:

![](screenshots/scrn3.png?raw=true)

Get the status of my deployment:

![](screenshots/scrn4.png?raw=true)

We can now get that CLUSTER-IP to try making an example request to my deployed service from local machine:

![](screenshots/scrn5.png?raw=true)

This shows that my deployment of a simple contenerized REST API model is working.

Scaling and management of the running container can be now managed using Kubernetes cluster.



   
