import re
import os
from abc import ABC, abstractmethod

name = []
email = []
password = []

class Menu(ABC):
    def menu():
        print('=' * 50)
        print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
        print('1. Detail Anda')
        print('2. Ubah Nama')
        print('3. Jumlah Data pada File')
        print('4. Save Data pada File')
        print('5. Buat Data Baru')
        print('6. Keluar')

    @abstractmethod
    def pilihan(self):
        pass

class One(Menu):
    def pilihan(self):
        if name:
            for i in range (len(name)):
                print(f'Nama : {name[i]}')
                print(f'Email :{email[i]}')
                print(f'Password :{password[i]}')
        else:
            print('Data Saat Ini Kosong')  

class Two(Menu):
    def pilihan(self):
        if name:
            for i in range (len(name)):
                nama = input("Silahkan input nama baru: ")
                name[i] = nama

        else:
            print('='*50)
            print('Data Saat Ini Kosong')  
            
class Three(Menu):
    def pilihan(self):
        file_name = input("Masukkan Nama File: ")
        try:
            with open(file_name + ".txt", "r") as file:
                isi = file.read()
                total = isi.count("Nama")
                print("Berhasil")
                print(f"Jumlah data pada file: {total} Data")
        except:
            print(f"Tidak terdapat file dengan Nama {file_name}.txt")
            print("Jumlah data pada file : 0 data")  
class Four(Menu):
    def pilihan(self):
        
        if name:
            file_name = input("Silahkan Masukkan Nama File : ") + '.txt'
            print("Berhasil")
            if os.path.exists(file_name):
                for i in range (len(name)):
                    with open(file_name, 'a') as file:
                        file.write(f"\n|Nama\t\t: {name[i]}\n")
                        file.write(f"|Email\t\t: {email[i]}\n")
                        file.write(f"|Password\t: {password[i]}\n")
                        file.write(f"=" * 100)
            
            else:
                with open(file_name, 'x') as file:
                     for i in range (len(name)):
                        file.write("+"+"=" * 100)
                        file.write(f"\n|Data Yang Tersimpan\n")
                        file.write("+"+"=" * 100)
                        file.write(f"\n|Nama\t\t: {name[i]}\n")
                        file.write(f"|Email\t\t: {email[i]}\n")
                        file.write(f"|Password\t: {password[i]}\n")
                        file.write("+"+"=" * 100)
        else:
            print('Data Saat Ini Kosong')

class Five(Menu):
    def pilihan(self):
        nama = input("Silahkan Masukkan Nama Anda : ")
        name.append(nama)
        while True:
            emaill = input("Silahkan Masukkan Email Anda : ")
            if re.fullmatch("^[a-z]{1,}(@student\.unhas\.ac\.id$)", (emaill)):
                email.append(emaill)
                
                break
            else:
                print('=' * 50)
                print("Email Yang Anda Masukkan Salah")
                print('=' * 50)
        while True:
            passwordd = input("Silahkan Masukkan Password Anda : ")
            if re.fullmatch(".{8,20}", (passwordd)):
                if re.findall("[A-Z]+", (passwordd)) and re.findall("[a-z]+", (passwordd)) and re.findall("[0-9]+", (passwordd)):
                    password.append(passwordd)
                    break
                else:
                    print('=' * 50)
                    print("Password Yang anda masukkan terlalu lemah")
                    print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                    print('=' * 50)
            else:
                print('=' * 50)
                print("Password Harus Memiliki Panjang 8-20 Karakter")
                print('=' * 50)
class Six(Menu):
    def pilihan(self):
        print('=' * 50)
        print('Sampai Jumpa Lagi')