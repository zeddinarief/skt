import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

print("menu :")
print("1. tampil semua sensor")
print("2. tampil sensor suhu")
print("3. tampil sensor kelembaban")
print("4. tampil sensor kadar CO")
menu = input("pilih menu no : ")

if menu == "1" :
	proxy.getAllsensor()

elif menu == "2" :
	proxy.getsensorsuhu()

elif menu == "3" :
	proxy.getsensorkelembaban()

elif menu == "4" :
	proxy.getsensorCO()

else:
	print("menu tidak ada")