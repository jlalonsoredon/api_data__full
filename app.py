from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def healthcheck():
    return {'status': 'ok'}

@app.route('/api/v1/states', methods=['GET'])
def get_states():
    return {'states': [
        {'id': 0,
         'provincia': 'Álava',
         'costa': False,
         'montaña': True
        },
        {'id': 1,
         'provincia': 'Albacete',
         'costa': False,
         'montaña': False
        },
        {'id': 2,
         'provincia': 'Alicante',
         'costa': True,
         'montaña': False
        },
        {'id': 3,
         'provincia': 'Almería',
         'costa': True,
         'montaña': False
        },
        {'id': 4,
         'provincia': 'Asturias',
         'costa': True,
         'montaña': True
        },
        {'id': 5,
         'provincia': 'Ávila',
         'costa': False,
         'montaña': True
        },
        {'id': 6,
         'provincia': 'Badajoz',
         'costa': False,
         'montaña': False
        },
        {'id': 7,
         'provincia': 'Barcelona',
         'costa': True,
         'montaña': False
        },
        {'id': 8,
         'provincia': 'Burgos',
         'costa': False,
         'montaña': True
        },
        {'id': 9,
         'provincia': 'Cáceres',
         'costa': False,
         'montaña': False
        },
    ]}

@app.route('/api/v1/predict', methods=['GET'])
def get_prediction():
    provincia = request.args.get('provincia')
    return {'prediction': 500} 

app.run()
