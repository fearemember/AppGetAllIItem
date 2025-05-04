'''
Clase que gestiona todo lo relacionado con la gestion de archivos
'''
from requirements import ensure_package

ensure_package("colorama")
ensure_package("zipfile")
ensure_package("os")
ensure_package("pathlib")
ensure_package("re")
ensure_package("datetime")

import os
import re
from pathlib import Path
import zipfile
import datetime
from colorama import init, Fore, Style

all_format_img = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.heif', '.heic', '.svg', '.pdf', '.eps', '.ai', '.raw', '.ico']
all_format_audio = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac', '.aiff', '.opus', '.amr', '.mid', '.ra']
all_format_document = ['.doc', '.docx', '.odt', '.pdf', '.txt', '.rtf', '.md', '.tex', '.epub', '.mobi', '.xls', '.xlsx', '.csv', '.ppt', '.pptx', '.pps', '.ppsx']

def create_folder_and_zip():
    name = input("Escribe el nombre de la carpeta que se creara\n")
    ruta =  Path(Path().absolute(),name)
    try:
        ruta.mkdir(exist_ok=False)
    except:
        zip_create = zipfile.ZipFile(Path(ruta, name + "_" + str(datetime.date.today()) + ".zip"), 'a')
        print(f"{Fore.YELLOW}La ruta ya existe en el sistema, se sobreescribirá sobre la misma ruta.{Fore.RESET}")
    else:
        zip_create = zipfile.ZipFile(Path(ruta,name+"_"+str(datetime.date.today())+".zip"),'w')
        print(f"{Fore.GREEN}Se ha creado la ruta y el contenedor zip:\n{ruta}{Fore.RESET}")
    return zip_create

def get_path_check():
    while True:
        ruta = input("Escribe la ruta raiz desde la que desea obtener todas las imagenes:\n")
        if Path(ruta).exists():
            return Path(ruta)
        else:
            print(F"{Fore.RED}La ruta que has introducido no existe{Fore.RESET}")

def get_type_item():
    while True:
        select = input(f"Elija que tipo de archivo desea almacenar en el zip\n[1] Imagenes:{Fore.BLUE}"
                           f"\n\t{"\t".join(all_format_img)}\n{Fore.RESET}[2] Audios:{Fore.BLUE}"
                           f"\n\t{"\t".join(all_format_audio)}\n{Fore.RESET}[3] Document:{Fore.BLUE}"
                           f"\n\t{"\t".join(all_format_document)}"
                           f"\n{Fore.RESET}[4] Ingresar formatos especifico."
                           f"\nElija una de las opciones anteriores:\n")
        match select:
            case "1":
                return all_format_img
            case "2":
                return all_format_audio
            case "3":
                return all_format_document
            case "4":
                custom_search = input("Escriba los formatos que desea buscar, puede ingresar varios separados por un espacio \' \':\nEjemplo:\'.jpg .gif\'\n")
                all_custom_format = []
                list_option_custom = custom_search.split(" ")
                pattern = r"^\.\w+"
                for custom_option in list_option_custom:
                    if re.search(pattern,custom_option):
                        all_custom_format.append(custom_option)
                        print(f"{Fore.GREEN}Se ha añadido \'{custom_option}\' al sistema de busqueda\n{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}El formato \'{custom_option}\' no es un formato valido\n{Fore.RESET}")
                return all_custom_format

            case _:
                os.system('cls')
                print("Opción invalida")

def look_all_directories_by_format(ruta,type_element):
    list_item_added = []
    for ruta_element, folder_element, file_element in os.walk(ruta):
        for file_item in file_element:
            for formato_item in type_element:
                if file_item.upper().endswith(formato_item.upper()):
                    list_item_added.append(Path(ruta_element,file_item))
    return list_item_added

def save_item_in_zip(zip_created,list_item_added):

    for item in list_item_added:
        archivos_existentes = set(zip_created.namelist())
        arcname = f"{item.suffix.replace(".", "_")}/{item.parent.name}_{item.name}"
        if arcname in archivos_existentes:
            print(f"{Fore.YELLOW}El archivo: {item} no se almacenará por que es una duplica de un archivo ya almacenado.{Fore.RESET}")
        else:
            try:
                zip_created.write(item, "/"+arcname)
                print(f"{Fore.GREEN}Se ha añadido {item.name}{Fore.RESET}")
            except UserWarning:
                print(f"{Fore.RED}El archivo: {item} no se almacenará por que esta duplicado en el origen.{Fore.RESET}")

    zip_created.close()




