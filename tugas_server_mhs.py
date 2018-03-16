#import library flask
from flask import Flask, request , jsonify , abort
import json

#inisiasi app flask sebagai server
app = Flask("Hello App")

#data mahasiwa nim,nama,prodi
data_mhs = [
    {
        "NIM" : 111,
        "Nama" : "ryan",
        "Prodi" : "TIF"
    },
    {
        "NIM" : 222,
        "Nama" : "adit",
        "Prodi" : "TIF"
    },
    {
        "NIM" : 333,
        "Nama" : "fahmi",
        "Prodi" : "TIF"
    }

]

#fungsi untuk tampil semua data mhs
@app.route('/mhs', methods=['GET'])
def handle_get_all():
    #return json.dumps(data_mhs)
    return jsonify({"data_mhs": data_mhs})

#fungsi untuk tampil satu data mhs
@app.route('/mhs/<int:nim>', methods=['GET'])
def handle_get_mhs(nim):
    for i in range(0, len(data_mhs)):
        if nim == data_mhs[i]["NIM"]:
            return jsonify({"data_mhs": data_mhs[i]})
            #return json.dumps(data_mhs[i])
    #jika nim tidak ditemukan
    #abort(404)
    return "NIM tidak Terdaftar"


#fungsi untuk tambah mhs 
@app.route('/mhs', methods=['POST'])
def tambah_mhs():
    #baca body request
    nim = request.json['NIM']
    nama = request.json['Nama']
    prodi = request.json['Prodi']
    #buat dict baru
    mhs_baru = {
        'NIM' : nim,
        'Nama' : nama,
        'Prodi' : prodi
    }
    #tambah ke list data mhs
    data_mhs.append(mhs_baru)    
    return jsonify({"data_mhs": data_mhs})

#fungsi untuk tambah mhs 
@app.route('/mhs/<int:nim>', methods=['PUT'])
def update_mhs(nim):
    for i in range(0, len(data_mhs)):
        if nim == data_mhs[i]['NIM']:    
            data_mhs[i]['NIM'] = request.json['NIM']
            data_mhs[i]['Nama'] = request.json['Nama']
            data_mhs[i]['Prodi'] = request.json['Prodi']
            return jsonify({'data_mhs': data_mhs})
    return "NIM tidak terdaftar"

@app.route('/mhs/<int:nim>', methods=['DELETE'])
def delete_mhs(nim):

    for i in range(0, len(data_mhs)):
        if nim == data_mhs[i]['NIM']:
            #hapus data_mahasiswa index ke i
            data_mhs.remove(data_mhs[i])
            return "Deleted"
    #jika nim tidak ditemukan
    return "NIM tidak terdaftar"


#jalankan server Flask
app.run(port=7777)

