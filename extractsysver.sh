unzip $1
ninfs cia updates/000400DB00017502.cia cver1
ninfs cia updates/000400DB00016502.cia nver1
ninfs ncch cver1/0000.000000*/decrypted.cfa cver2
ninfs ncch nver1/0000.000000*/decrypted.cfa nver2
python extractsysver.py
rm -rf updates
umount cver2
umount nver2
umount cver1
umount nver1