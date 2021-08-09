#Aluno : João Victor Rodrigues dos Santos

#Obs acessar pelo local host:80/docs
import pickle
from fastapi import FastAPI
app = FastAPI()

@app.post('/model')
## Coloque seu codigo na função abaixo

async def titanic(Sex:int,Age:float, Lifeboat:int, Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid:
        titanic = pickle.load(fid)

    predicao = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist()

    try:
        return {
            'status': 200,
            'survived': bool(predicao[0]),
            'message': 'Modelo Titanic Executado',
        }
    except Exception:
        return {
            'message': 'Modelo Titanic não Executado'
        }

@app.get('/model')
def get():
    return {'hello':'test'}
