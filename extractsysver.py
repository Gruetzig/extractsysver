cver = open("cver2/romfs/version.bin",'rb')
cver.seek(1)
cverminor = int.from_bytes(cver.read(1), byteorder='big')
cver.seek(2)
cvermajor = int.from_bytes(cver.read(1), byteorder='big')
nver = open("nver2/romfs/version.bin", 'rb')
nver.seek(2)
nverversion = int.from_bytes(nver.read(1), byteorder='big')
print(f"{cvermajor}.{cverminor}.0-{nverversion}K")
cver.close()
nver.close()


