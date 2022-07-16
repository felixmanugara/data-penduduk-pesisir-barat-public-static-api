from scrape import cleandata2019_1, cleandata2019_2, cleandata2020_1, cleandata2020_2, cleandata2021_1
from flask import Flask, render_template, jsonify, request

api = Flask(__name__)

def create_json(data,option):
    dump = data
    datain = []
    if option == 1:
        data_length = len(data['desa kelurahan']) - 1
        for index in range(0, data_length):
            insert = {'nama kecamatan': dump['nama kecamatan'][index], 
                      'desa kelurahan': dump['desa kelurahan'][index],
                      'jumlah pria': dump['jumlah pria'][index],
                      'jumlah wanita': dump['jumlah wanita'][index],
                      'kepala keluarga': dump['kepala keluarga'][index],
                      'jumlah penduduk:': dump['jumlah penduduk'][index]}
            
            datain.append(insert)

    elif option == 2:
         data_length = len(data['desa kelurahan'])
         for index in range(0, data_length):
            insert = {'desa kelurahan': dump['desa kelurahan'][index],
                      'jumlah pria': dump['jumlah pria'][index],
                      'jumlah wanita': dump['jumlah wanita'][index],
                      'kepala keluarga': dump['kepala keluarga'][index],
                      'jumlah penduduk:': dump['jumlah penduduk'][index]}
            
            datain.append(insert)
    
    return datain


@api.route("/")
def home():
    return render_template('index.html')

@api.route("/2019-semester-1", methods=['GET','POST'])
def data_penduduk_2019_1():
    try:
        data = create_json(cleandata2019_1,option=1)
        if request.method == 'GET':
            return jsonify(data)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(data[int(id)])
            
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
        data = create_json(cleandata2019_2,option=2)
        if request.method == 'GET':
            return jsonify(data)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(data[int(id)])
            
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
        data = create_json(cleandata2020_1,option=1)
        if request.method == 'GET':
            return jsonify(data)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(data[int(id)])
            
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
        data = create_json(cleandata2020_2,option=2)
        if request.method == 'GET':
            return jsonify(data)

        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(data[int(id)])
            
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
        data = create_json(cleandata2021_1,option=2)
        if request.method == 'GET':
            return jsonify(data)
    
        elif request.method == 'POST':
            id = request.args.get('id')
            return jsonify(data[int(id)])
            
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

