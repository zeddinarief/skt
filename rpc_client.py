import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

#panggil fungsi
hasil = proxy.penjumlahan(20,10)
print(hasil)