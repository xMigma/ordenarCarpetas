import os
import shutil
from extensiones import extensiones

def obtener_ruta():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(
                key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')


def ordenar():
    ruta = obtener_ruta() + "\\"

    for i in extensiones:
        try:
            os.makedirs(ruta + i)
        except FileExistsError:
            pass    

    for archivo in os.listdir(ruta):
        nombre_archivo, ext = os.path.splitext(archivo)
        for tipo in extensiones:
                for i in extensiones[tipo]: 
                    if ext == i:
                        try:
                            shutil.move(ruta + archivo,
                                   ruta + tipo)
                            print("El archivo" , archivo , "se ha movido a" , tipo)       
                        except:
                            print("El archivo" , archivo , "no ha podido moverse")
                            shutil.move(ruta + archivo,
                                   ruta + 'Duplicados')                 




