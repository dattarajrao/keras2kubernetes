import os
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.preprocessing import image
import json

# load the appropriate Keras model
MODEL_PATH = 'model.h5'

# check if user provided a model file else use default
if os.path.isfile('/model/model.h5'):
    MODEL_PATH = '/model/model.h5'

# Load the model from saved file
classifier = keras.models.load_model(MODEL_PATH)
classifier._make_predict_function()
print("Model file %s loaded in memory."%MODEL_PATH)

# find input image dimesions from model
modj = json.loads(classifier.to_json())
IMGH = modj['config'][0]['config']['batch_input_shape'][1]
IMGW = modj['config'][0]['config']['batch_input_shape'][2]

# create the main application
app = Flask(__name__, static_url_path='')

UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(tf.__version__)

# Make prediction for image and populate result dictionary
def make_prediction(filepath):
    result = {}
    result['filename'] = filepath
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filepath)
    test_image = image.load_img(filepath, target_size = (IMGW, IMGH))
    test_image = image.img_to_array(test_image)/255.
    print(test_image.shape)
    test_image = np.expand_dims(test_image, axis = 0)
    result['answer'] = classifier.predict(test_image)[0]
    return result

def delete_file(filepath):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filepath)
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print("The file does not exists")

@app.route('/')
def myindex():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    # save image to folder on disk
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    # Make the Prediction with saved image
    result = make_prediction(file.filename)
    return render_template('index.html', result=result)

@app.route('/inference', methods=['POST'])
def inference():
    file = request.files['image']
    # save image to folder on disk
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    # Make the Prediction with saved image
    result = make_prediction(file.filename)
    delete_file(file.filename)
    return render_template('index.json', result=result)

@app.route('/model')
def get_model():
    return classifier.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001, debug=False, threaded=False)
