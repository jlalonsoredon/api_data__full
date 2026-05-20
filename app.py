import os
import pickle

import numpy as np
import pandas as pd
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

with open(os.path.join(os.path.dirname(__file__), 'models', 'model2.pkl'), 'rb') as f:
    model = pickle.load(f)

# del csv crea un array con las provincias y si tiene costa  en las columna es_costa Y/o montaña en es_montana
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'df_final2.csv'))
provincias = (
    df[['location_name', 'es_costa', 'es_montana']]
    .drop_duplicates('location_name')
    .sort_values('location_name')
    .reset_index(drop=True)
    .rename(columns={'location_name': 'provincia', 'es_costa': 'costa', 'es_montana': 'montaña'})
    .assign(id=lambda d: d.index)
    [['id', 'provincia', 'costa', 'montaña']]
    .to_dict(orient='records')
)

@app.route('/', methods=['GET'])
def healthcheck():
    return {'status': 'ok'}

@app.route('/api/v1/states', methods=['GET'])
def get_states():
    return {'states': provincias}


@app.route('/api/v1/predict', methods=['GET'])
def get_prediction():
    provincia       = request.args.get('provincia', '')
    surface         = float(request.args.get('surface', 0))
    bedrooms        = int(request.args.get('bedrooms', 0))
    restrooms       = int(request.args.get('restrooms', 0))
    tiene_ascensor  = int(request.args.get('tiene_ascensor', 0))
    tiene_parking   = int(request.args.get('tiene_parking', 0))
    tiene_piscina   = int(request.args.get('tiene_piscina', 0))
    tiene_terraza   = int(request.args.get('tiene_terraza', 0))

    data = pd.DataFrame([{
        'surface':        surface,
        'bedrooms':       bedrooms,
        'restrooms':      restrooms,
        'location_name':  provincia,
        'tiene_ascensor': tiene_ascensor,
        'tiene_parking':  tiene_parking,
        'tiene_piscina':  tiene_piscina,
        'tiene_terraza':  tiene_terraza,
    }])

    prediction = model.predict(data)[0]
    return {'prediction': round(float(prediction), 2)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
