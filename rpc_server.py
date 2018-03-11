# import xmlrpc
import xmlrpc.server

# inisiasi servernya
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 1409) )

# Definisikan procedure/fungsi yang akan dipanggil di client
def penjumlahan(a,b):
    return (a+b)

# Daftarkan fungsi yang akan dipanggil client
server.register_function(penjumlahan, 'penjumlahan')
# Jalankan server
server.server_forever()
