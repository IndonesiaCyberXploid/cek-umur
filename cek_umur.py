import datetime as dt
import os
import time
from time import sleep as sek
from os import system as o

logo = ('''
====================================
Author : Angga Xploid
Team   : INDONESIA CYBER XPLOID
YOUTUBE: INDONESIA CYBER XPLOID
====================================\n
''')

os.system('clear')
print (logo)
tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
hari_ini = dt.date.today()
print(f'Hari ini tanggal : {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f'Tanggal lahir anda : {tanggal_lahir}')
print(f'Hari anda lahir : {tanggal_lahir : %A}')
print(f'Umur anda : {umur_tahun} tahun, {umur_bulan_sisa} bulan')