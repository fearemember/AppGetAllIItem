
from requirements import ensure_package

ensure_package("time")
ensure_package("os")
ensure_package("pyfiglet")
ensure_package("colorama")


from  CompressAllIItemFromDirectory import *
import time
import os
import pyfiglet
from colorama import init, Fore, Style



def welcome():
    ascii_banner = pyfiglet.figlet_format("FEAREMEMBER")
    print(ascii_banner)
    print("-" * 100)
    print(f"Hola bienvenido a esta herramienta desarrollada por {Fore.BLUE}Pedro Moreno a.k.a @Fearemember{Fore.RESET}\n"
          f"Esta herramienta te permite almacenar todos los archivos de un mismo tipo en un zip\n"
          f"Deberás proporcionar la URL desde la que deseas iniciar el analisis.")
    print("-"*100+"\n")

def menu():
    result = 1
    while result!="0":
        type_item = get_type_item()
        zip_file_created =create_folder_and_zip()
        path_research = get_path_check()
        initial_time = time.time()
        list_item = look_all_directories_by_format(path_research,type_item)
        save_item_in_zip(zip_file_created,list_item)
        print("-" * 150)
        final_time = time.time()
        print(f"Tiempo en completar el proceso: {Fore.BLUE}\n{round((final_time-initial_time)/60,2)} minutos{Fore.RESET}")
        result = input("Se ha completado el proceso si quiere cerrar el programa escriba \"0\"\n")
        os.system("cls")
    print("Gracias por todo.")

