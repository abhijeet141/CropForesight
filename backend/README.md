# CropForesight BackEnd


The repository for the backend of the [Crop Foresight project](https://github.com/abhijeet141/CropForesight) made using Pydantic and FastAPI.

By using various parameters like Nitrogen, Phosphorous, Potassium, rainfall, humidity, temperature and pH it predicts the most optimal crop for the land from among 22 crops ranging from rice or apples to cotton or lentils using a Gaussian Naive Bayes model

<br>
<div align = 'center'>

 <img src="https://img.shields.io/github/repo-size/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
 <img src="https://img.shields.io/github/issues/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-closed-raw/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr-closed/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr-raw/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  <img src="https://img.shields.io/github/contributors-anon/abhijeet141/CropForesight_BackEnd?style=for-the-badge" />
  
</div>


## Table of Contents


1. [Technologies Used](#technologies-used)
1. [Running the Project Locally](#runnning-the-project-locally)
1. [Contributing](#contributing)
1. [License](#license)
1. [Deployment](#deployment)


## Technologies Used:


 ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
 ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)


## Runnning the Project Locally:


#### Clone the backend repository:

```
git clone https://github.com/abhijeet141/CropForesight_BackEnd.git
```

#### Change to the CropForesight_BackEnd directory:

```
cd CropForesight_BackEnd
```

#### Install the required dependencies:

```
pip install -r requirements.txt
```

#### Run the backend:

```
uvicorn main:app --reload
```

##### Open the website in your browser at http://localhost:3000.

## Contributing

Refer to the contribution guidelines [here](https://github.com/abhijeet141/CropForesight#-contributing)


## License

The entire project is licensed under the [MIT License](https://opensource.org/license/mit/)

## Deployment


You can access the deployed frontend at: 
### https://crop-foresight-front-end.vercel.app/.
