import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing.image import load_img, img_to_array
from io import BytesIO

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_alexnet = load_model('alexnet_model.h5')

class_names = [
    'Tomato Bacterial Spot', 'Tomato Early Blight', 'Tomato Late Blight', 
    'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot',
    'Tomato Spider Mites', 'Tomato Target Spot', 
    'Tomato Yellow Leaf Curl Virus', 'Tomato Mosaic Virus', 
    'Tomato Healthy'
]

@app.get('/')
def welcome():
    return {
        'success': True,
        'message': 'Server for multimodel tomato disease classification using 10 classes is up and running successfully.'
    }

@app.post('/predict')
async def predict_disease(fileUploadedByUser: UploadFile = File(...)):
    try:
        contents = await fileUploadedByUser.read()
        
        image = load_img(BytesIO(contents), target_size=(227, 227, 3))
        image_array = img_to_array(image) / 255
        img_to_arr_expand_dim = np.expand_dims(image_array, axis=0)
                
        prediction = model_alexnet.predict(img_to_arr_expand_dim)[0]
        prediction_argmax = np.argmax(prediction)
        
        # Get predicted class and confidence
        predicted_class = class_names[prediction_argmax]
        confidence = np.max(prediction) * 100
        
        return {
            'success': True,
            'predicted_result': predicted_class,
            'confidence': f'{confidence:.2f}%',
            'message': f'Status of the Tomato Plant Leaf Disease: {predicted_class} with a confidence of {confidence:.2f}%'
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }
