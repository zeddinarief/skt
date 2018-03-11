import http.client
import json
ip_server = "127.0.0.1"
port_server = 7777
def get_mhs():
	#kirim request GET dgn url "/mhs"
	#inisiasi koneksi ke server
	conn = http.client.HTTPConnection(ip_server, port=port_server)

	#kirim request ke server
	conn.request('GET', '/mhs')
	#baca respon
	respon = conn.getresponse().read()
	print(respon.decode('ascii'))

def tambah_mhs():
	#kirim request GET dgn url "/mhs"
	#inisiasi koneksi ke server
	conn = http.client.HTTPConnection(ip_server, port=port_server)

	#definisi kan header
	header = {"Content-type" : "application/json"}

	#definisikan body
	mhs_baru = {"NIM" : 210, "Nama" : "canda"}

	#kirim request ke server
	conn.request('POST', '/mhs', body=json.dumps(mhs_baru),headers=header)
	#baca respon
	respon = conn.getresponse().read()
	print(respon.decode('ascii'))

tambah_mhs()
get_mhs()