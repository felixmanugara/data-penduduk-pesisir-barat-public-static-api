from flask import Flask, render_template, jsonify, request
import json


filenames = ['json/data_penduduk_2019_sem-1.json','json/data_penduduk_2019_sem-2.json','json/data_penduduk_2020_sem-1.json','json/data_penduduk_2020_sem-2.json','json/data_penduduk_2021_sem-1.json']

files = [open(filename, 'r') for filename in filenames]
sem1_2019 = json.loads(files[0].read())
sem2_2019 = json.loads(files[1].read())
sem1_2020 = json.loads(files[2].read())
sem2_2020 = json.loads(files[3].read())
sem1_2021 = json.loads(files[4].read())


api = Flask(__name__)


@api.route("/")
def home():
    return render_template('index.html')

@api.route("/2019-semester-1", methods=['GET','POST'])
def data_penduduk_2019_1():
    try:
        if request.method == 'GET':
            return jsonify(sem1_2019)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(sem1_2019[int(id)])
            
    except IndexError:
        response = jsonify({'status':'id error, masukkan id antara 0 - 129'})
        response.status_code = 400
        return response
        
    except ValueError:
        response = jsonify({'status':'Query parameter value salah, masukkan parameter id dengan angka'})
        response.status_code = 404
        return response
        
    except TypeError:
        response = jsonify({'status':'Query parameter salah, gunakan Query parameter id'})
        response.status_code = 400
        return response

@api.route("/2019-semester-2", methods=['GET','POST'])
def data_penduduk_2019_2():
    try:
        if request.method == 'GET':
            return jsonify(sem2_2019)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(sem2_2019[int(id)])
            
    except IndexError:
        response = jsonify({'status':'id error, masukkan id antara 0 - 129'})
        response.status_code = 400
        return response
        
    except ValueError:
        response = jsonify({'status':'Query parameter value salah, masukkan parameter id dengan angka'})
        response.status_code = 404
        return response
        
    except TypeError:
        response = jsonify({'status':'Query parameter salah, gunakan Query parameter id'})
        response.status_code = 400
        return response
    
@api.route("/2020-semester-1", methods=['GET','POST'])
def data_penduduk_2020_1():
    try:
        if request.method == 'GET':
            return jsonify(sem1_2020)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(sem1_2020[int(id)])
            
    except IndexError:
        response = jsonify({'status':'id error, masukkan id antara 0 - 129'})
        response.status_code = 400
        return response
    
    except ValueError:
        response = jsonify({'status':'Query parameter value salah, masukkan parameter id dengan angka'})
        response.status_code = 404
        return response
        
    except TypeError:
        response = jsonify({'status':'Query parameter salah, gunakan Query parameter id'})
        response.status_code = 400
        return response
 
@api.route("/2020-semester-2", methods=['GET','POST'])
def data_penduduk_2020_2():
    try:
        if request.method == 'GET':
            return jsonify(sem2_2020)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(sem2_2020[int(id)])
            
    except IndexError:
        response = jsonify({'status':'id error, masukkan id antara 0 - 129'})
        response.status_code = 400
        return response
        
    except ValueError:
        response = jsonify({'status':'Query parameter value salah, masukkan parameter id dengan angka'})
        response.status_code = 404
        return response
        
    except TypeError:
        response = jsonify({'status':'Query parameter salah, gunakan Query parameter id'})
        response.status_code = 400
        return response
    
@api.route("/2021-semester-1", methods=['GET','POST'])
def data_penduduk_2021_1():
    try:
        if request.method == 'GET':
            return jsonify(sem1_2021)
    
        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(sem1_2021[int(id)])
            
    except IndexError:
        response = jsonify({'status':'id error, masukkan id antara 0 - 129'})
        response.status_code = 404
        return response
        
    except ValueError:
        response = jsonify({'status':'Query parameter value salah, masukkan parameter id dengan angka'})
        response.status_code = 400
        return response
        
    except TypeError:
        response = jsonify({'status':'Query parameter salah, gunakan Query parameter id'})
        response.status_code = 404
        return response
            
        
if __name__ == "__main__":
    api.run()

