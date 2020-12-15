from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def top():
    json = {
        'response' : 'json'
    }
    return jsonify(json)

@app.route('/map/mapping', methods=['GET'])
def mapMapping():
    json = {
        "location":[
            {
                "name": "サンプルA",
                "lat": 34.69811068811861,
                "lng": 135.49675583839417
            },
            {
                "name": "サンプルB",
                "lat": 34.695287967969016, 
                "lng": 135.48843026161194
            }, 
            {
                "name": "サンプルC",
                "lat": 34.696734624073216, 
                "lng": 135.48845171928406
            }
        ]
    }    
    return jsonify(json)    

@app.route('/test/api', methods=['GET'])
def testAPI():
    json = {
        "train": {
            "京阪線": {
            "response":"京阪電車が１０分遅延しているので早めにいった方がいいで",
            "face":"smile"
            },
            "京阪線": {
            "response":"今は遅延してないで",
            "face":"smile"
            }
        },
        "meteo": {
            "明日の天気": {
            "response": "明日は晴れるみたいやでー",
            "face":"smile"
            },
            "明日の降水確率":{
            "response": "明日の降水確率90%やから傘持っていきや",
            "face": "sad"
            },
            "今日の天気":{
            "response":"今日の11時頃から雨降る予定やから傘持っていきやー",
            "face": "trouble"
            },
            "今日の天気":{
            "response": "今日は雨降らんみたいやで",
            "face": "smile"
            },
            "今週の天気":{
            "response": "今週は土日に雨降るみたいやで。雨具用意しときや",
            "face": "trouble"
            }
        },
        "meteo_train":{
            "明日の電車":{
            "response":"明日は雨が降るから遅れるかもしれんで",
            "face":"sad"
            },
            "台風明日電車":{
            "response":"明日台風来るから午前中運休やでー",
            "face": "fear"
            }
        },
        "youtube": {
            "お勧めの動画":{
            "response":"オススメは本当にあった怖い話やでー",
            "face": "fear"
            }
        }
    }    
    return jsonify(json)    

if __name__ == "__main__":
    app.run(debug=True)    