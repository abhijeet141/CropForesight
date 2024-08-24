from fastapi import FastAPI  # it imports FastAPI class from the fastapi module
from fastapi.middleware.cors import (
    CORSMiddleware,
)  # it imports CORSMiddleware from fastapi.middleware.cors module

# CORS-CrossOriginResourceSharing it is a security mechanism implemented by web browser to restrict cross origin request from web application
# When a web browser is running on one origin(domain,protocol and port) and it tries to access resource from other origin the browser will block the request by default
# This is to prevent security vulnerabilities
# CORSMiddleware class is a middleware that is used with fastApi to enable CORS for our web application
# By adding this middleware to our fast api application we can configure our api to accept cross origin request from specific origin
from pydantic import BaseModel  # it imports basemodel class from pydentic module

# pydentic provides data validation and setting management
# BaseModel is a baseclass that we can inherit from to define our own data model
# We use this to define the structure of the data that our API expects to receive as an input or to define the structure of data that our api will return as output
import pandas as pd  # to create dataframe object which allow us to work with tabular data
import pickle  # pickle provides a way to serialize and deserialize python objects serialize is a way of converting an object into a format that can be stored or transmitted while deserialize is a way to convert serialize data back to object

# it save our ml model as files which can be loaded and used in fastapi application
# when we tarin our ml model we fit it on a dataset and obtain a set of learned parameters that can be used to make prediction on new data these learned parameters can be saved as a file which can then be loaded and used to make prediction on new data
app = (
    FastAPI()
)  # when we call FastAPI() we create a new FastAPI application which is used to define our API endpoints, middleware and other configuration settings

origins = [
    "*"
]  # it is a parameter that can be passed to the fastapi instance to configure CORS settings
# origin is a list of string that represents the allowed origin for cross origin request
# by default cross origin request is blocked so origins=["*"] means any origins will be allowed to make cross origin request
# * is a wildcard character that represents any origin

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cropRecomendation = pd.read_csv("./Crop_recommendation.csv")

better_model = pickle.load(open("./crop_recomendation.pkl", "rb"))


class cropInfo(BaseModel):
    nitrogen: int
    phosphorus: int
    potassium: int
    temperature: int
    humidity: int
    ph: int
    rainfall: int


@app.post("/predict")
async def predict_crop(cropInfo: cropInfo):
    nitrogen_value = cropInfo.nitrogen
    phosphorus_value = cropInfo.phosphorus
    potassium_value = cropInfo.potassium
    temperature_value = cropInfo.temperature
    humidity_value = cropInfo.humidity
    ph_value = cropInfo.ph
    rainfall_value = cropInfo.rainfall

    prediction = better_model.predict(
        pd.DataFrame(
            [
                [
                    nitrogen_value,
                    phosphorus_value,
                    potassium_value,
                    temperature_value,
                    humidity_value,
                    ph_value,
                    rainfall_value,
                ]
            ],
            columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
        )
    )
    print(prediction)

    return {"result": prediction[0]}
