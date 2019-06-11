FROM python:3.6
#FROM paperspace/fastai:1.0-CUDA9.2-base-3.0-v1.0.6

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ app/
COPY app/data/train.csv app/
COPY app/data/val.csv app/
COPY app/data/data_clas.pkl app/
ADD app/data/models/twitter-sentiment-classifier.pth app/models/twitter-sentiment-classifier.pth
ADD app/data/models/twitter-sentiment-enc.pth app/models/twitter-sentiment-enc.pth

#RUN python app/rest_api.py

EXPOSE 3000

CMD ["python", "app/rest_api.py"]