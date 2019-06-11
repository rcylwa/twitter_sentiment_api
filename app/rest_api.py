from flask import Flask, request, jsonify # loading in Flask
from fastai.text import *
import pandas as pd

# creating a Flask application
app = Flask(__name__)

# Load the model
df_train = pd.read_csv('app/train.csv')
df_val = pd.read_csv('app/val.csv')
#data_clas = TextClasDataBunch.from_df('.', df_train, df_val, text_cols=0, label_cols=1, bs=32)
data_clas = load_data('.', 'app/data_clas.pkl', bs=32)
learn = text_classifier_learner(data_clas, arch=AWD_LSTM, pretrained=False, drop_mult=0.3, model_dir='.')
learn.load('app/models/twitter-sentiment-classifier')

# creating predict url and only allowing post requests.
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from Post request
    data = request.get_json()
    # Make prediction
    text = str(data['text'])
    # making predictions
    pred = learn.predict(text)
    #print(pred)
    # returning the predictions as json
    return jsonify(str(pred[0]))
    #return jsonify(str([torch.__version__, fastai.__version__]))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)