# Classification Wine Quality DeepLearning

Hello everyone, i make deep learning to predict **Quality** of **Wine Red**. I use `Python` and some library to make this deep learning. You can try this model in this website [Wine Quality](https://hafidh561.github.io/Classification-Wine-Quality-DeepLearning). I deploy this model use `FLASK Restful-API` in `Heroku`.  
_Note: The response API took too long, be patient please_

---

## Tutorial Install Model

1. First you must have install `Python` and `Python Package Index` in your computer
2. After that, open directory [**deploy_ml**](./deploy_ml/) in your terminal
3. You can use virtual environments, if you want
4. Type in your terminal `pip install -r requirements.txt -y` and wait untill done
5. After that, type in your terminal `python app.py`
6. Open [**index.html**](./index.html) and input some data

---

## Tutorial Use API

Connect to [Wine Quality API](https://winequalityapi.herokuapp.com/) and use `POST METHOD`.

1. `fixed_acidity` **(tartaric acid - g/dm3)**  
   Most acids involved with wine or fixed or nonvolatile (do not evaporate readily)
2. `volatile_acidity` **(acetic acid - g/dm3)**  
   The amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste
3. `citric_acid` **(g/dm3)**  
   Found in small quantities, citric acid can add ‘freshness’ and flavor to wines
4. `residual_sugar` **(g/dm3)**  
   The amount of sugar remaining after fermentation stops, it’s rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet
5. `chlorides` **(sodium chloride - g/dm3)**  
   The amount of salt in the wine
6. `free_sulfur_dioxide` **(mg/dm3)**  
   The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine
7. `total_sulfur_dioxide` **(mg/dm3)**  
   Amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine
8. `density` **(g/cm3)**  
   The density of water is close to that of water depending on the percent alcohol and sugar content
9. `ph`
   Describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale
10. `sulphates` **(potassium sulphate - g/dm3)**  
    A wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant
11. `alcohol` **(% by volume)**  
    The percent alcohol content of the wine

---

## Screenshots

- **Homepage**

![Index](./screenshots/screenshot_1.png 'Homepage')

- **Predict Appear**

![Predict](./screenshots/screenshot_2.png 'Predict Appear')

---

### License

[MIT](./LICENSE)

### Changelog

- **1.0 Classification Wine Quality DeepLearning**

© Developed by [hafidh561](https://github.com/hafidh561).
