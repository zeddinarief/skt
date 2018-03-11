#import library flask
from flask import Flask, request
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

#fungsi untuk tampil data mhs
@app.route('/mhs', methods=['GET'])
def handle_get():
	return json.dumps(data_mhs)

#fungsi untuk tambah mhs 
@app.route('/mhs', methods=['POST'])
def tambah_mhs():
	#baca body request
	nim = request.json['NIM']
	nama = request.json['Nama']
	#buat dict baru
	mhs_baru = {
		'NIM' : nim,
		'Nama' : nama
	}
	#tambah ke list data mhs
	data_mhs.append(mhs_baru)
	
	return "OK"
#jalankan server Flask
app.run(port=7777)

