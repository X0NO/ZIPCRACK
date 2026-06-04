from zipfile import ZipFile 
from colorama import Fore, Back, Style

import time

print(Style.RESET_ALL)

Path_ZIP = input("Path ZIP : ")
print(f"PATH ZIP :{Path_ZIP} ")

Path_PWD = input("Path PASSWORD : ")
print(f"PATH PASSWORD :{Path_PWD} ")
Password_list = []

file_password = open( Path_PWD , "r", encoding='utf-8-sig')
for line in file_password.readlines():
    Password_list.append(line.strip())
file_password.close()

start = time.time()

with ZipFile(Path_ZIP, "r" ) as zip:
    for pwd in Password_list :
        try:
            zip.setpassword(pwd.encode("utf-8"))
            result = zip.testzip()
            if result is None:
                print(f"{Fore.GREEN + pwd} : Valide")
                zip.extractall(path="uncompressed", pwd=pwd.encode("utf-8"))
                break
        except RuntimeError: 
            print(Fore.RED + f"{pwd} : Invalide")
    else :
        print("Aucun mot de passe")

end = time.time()

print(f"Temps de décompression : {end - start:.4f} ")