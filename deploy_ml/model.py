import pickle
import pandas as pd
import tensorflow as tf


def predict_model(fixed_acidity, volatile_acidity,
                  citric_acid, residual_sugar,
                  chlorides, free_sulfur_dioxide,
                  total_sulfur_dioxide, density,
                  ph, sulphates, alcohol):

    # Load Model
    scaler_x = pickle.load(open('./saved_model/scaler_x.pickle', 'rb'))
    scaler_y = pickle.load(open('./saved_model/scaler_y.pickle', 'rb'))
    model = tf.keras.models.load_model('./saved_model/model.h5')

    data = {
        'fixed_acidity': [fixed_acidity],
        'volatile_acidity': [volatile_acidity],
        'citric_acid': [citric_acid],
        'residual_sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free_sulfur_dioxide': [free_sulfur_dioxide],
        'total_sulfur_dioxide': [total_sulfur_dioxide],
        'density': [density],
        'ph': [ph],
        'sulphates': [sulphates],
        'alcohol': [alcohol]
    }

    df_predict = pd.DataFrame(data=data)
    x_predict = scaler_x.transform(df_predict)
    y_predict = model.predict(x_predict)
    y_predict = round(scaler_y.inverse_transform(y_predict)[0][0])

    y_predict = 0 if y_predict <= 0 else 10 if y_predict >= 10 else y_predict

    return y_predict
