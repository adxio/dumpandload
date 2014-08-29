from flask import Flask, jsonify
from vehicle import Truck
app = Flask(__name__)
host = '127.0.0.1'
port = 5000
debug = True

truk = Truck()
asli = truk.state()
jml = len(asli)

@app.route('/')
def home():
    data = {
        'status_code':200,
        'message':'OK'
        }
    return jsonify(responses=data,data=asli,car=jml)

@app.route('/position')
def position():
    data = {
        'status_code':200,
        'message':'OK'
    }
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'L':
            if jarak == 0 and arah == 'L':
                distance = jarak + 1
                head = 'D'
            else:
                distance = jarak - 1
                head = 'L'
        else:
            if jarak == 10 and arah =='D':
                distance = jarak - 1
                head = 'L'
            else:
                distance = jarak + 1
                head = 'D'
        pros = {
            'distance':distance,
            'head':head,
            'vehicle_number':vehicle_number
        }
        asli[i] = pros
    return jsonify(responses=data,data=asli,vehicle=jml)

@app.route('/load')
def load():
    pulang = []
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'L':
            pros = {
            'distance':jarak,
            'head':arah,
            'vehicle_number':vehicle_number
            }
            pulang.append(pros)
    res = {
        'status_code':200,
        'message':'OK'
    }
    return jsonify(response=res,data=pulang)

@app.route('/dump')
def dump():
    pulang = []
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'D':
            pros = {
            'distance':jarak,
            'head':arah,
            'vehicle_number':vehicle_number
            }
            pulang.append(pros)
    res = {
        'status_code':200,
        'message':'OK'
    }
    return jsonify(response=res,data=pulang)

if __name__ == '__main__':
    app.run(host, port, debug)