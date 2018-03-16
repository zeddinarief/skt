import http.client
import json
ip_server = "127.0.0.1"
port_server = 7777
#tampil seluruh mhs
def get_all_mhs():
    #kirim request GET dgn url "/mhs"
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #kirim request ke server
    conn.request('GET', '/mhs')
    #baca respon
    respon = conn.getresponse().read()
    print(respon.decode('ascii'))

#get satu mhs
def get_mhs(nim):
    
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #kirim request ke server
    conn.request('GET', '/mhs/'+nim)
    #baca respon
    respon = conn.getresponse().read()
    print(respon.decode('ascii'))

#add mhs
def tambah_mhs(nim , nama, prodi):
    
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #definisi kan header
    header = {"Content-type" : "application/json"}

    #definisikan body
    mhs_baru = {"NIM" : nim, "Nama" : nama, "Prodi" : prodi}

    #kirim request ke server
    conn.request('POST', '/mhs', body=json.dumps(mhs_baru),headers=header)
    #baca respon
    respon = conn.getresponse().read()
    print(respon.decode('ascii'))

def ubah_mhs(nim ,nama , prodi):
    
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #definisi kan header
    header = {"Content-type" : "application/json"}


    #definisikan body
    mhs_baru = {"NIM" : nim, "Nama" : nama, "Prodi" : prodi}

    #kirim request ke server
    conn.request('PUT', '/mhs/'+nim, body=json.dumps(mhs_baru),headers=header)
    #baca respon
    respon = conn.getresponse().read()
    print(respon.decode('ascii'))

def hapus_mhs(nim):
    
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #definisi kan header
    header = {"Content-type" : "application/json"}

    #kirim request ke server
    conn.request('DELETE', '/mhs/'+nim)
    #baca respon
    respon = conn.getresponse().read()
    print(respon.decode('ascii'))



print("menu")
print("1. Tambah Data Mahasiswa")
print("2. Ubah Data Mahasiswa")
print("3. Hapus Data Mahasiswa")
print("4. Tampil Data Seluruh Mahasiswa")
print("5. Tampil Data Satu Mahasiswa berdasar NIM")
menu = input("masukkan no menu : ")
if menu == "1":
    nim = input("NIM : ")
    nama = input("Nama : ")
    prodi = input("Prodi : ")
    tambah_mhs(nim,nama,prodi)

elif menu == "2":
    nim = input("data dari mahasiswa dg NIM : ")
    nama = input("Nama : ")
    prodi = input("Prodi : ")
    ubah_mhs(nim,nama,prodi)
elif menu == "3":
    nim = input("NIM : ")
    hapus_mhs(nim)
elif menu == "4":
    get_all_mhs()
elif menu == "5":
    nim = input("NIM : ")
    get_mhs(nim)
else:
    print("Menu tidak ada")
