import sys
from send2trash import send2trash
"""
    Mueve un archivo a la papelera de reciclaje. Simple y conciso.
    
    Este comando solicita confirmación antes de mover el archivo. Es compatible
    con sistemas operativos Windows, macOS y Linux aprovechando la librería `send2trash` por su portabilidad.

    Parámetros:
    file_path (str): Ruta o nombre del archivo a enviar a la papelera.

    Excepciones:
    - PermissionError: Si no se tienen permisos para mover el archivo.
    - Exception: Para cualquier otro error inesperado.



    --------------------------------------------------------------

    Moves a file to the recycle bin.
    
    This command asks for confirmation before moving the file. It is compatible
    with Windows, macOS, and Linux systems using the `send2trash` library due it portability.

    Parameters:
    file_path (str): Path or name of the file to be sent to the recycle bin.

    Exceptions:
    - PermissionError: If the user lacks permissions to move the file.
    - Exception: For any other unexpected errors.

  
"""

def move_to_trash(file_path):
    
    
    arch = file_path
    
    print(f"Seguro que querés mandar {arch} a la papelera? S(sí), N(No)")
    rta = input().lower()
    
    if rta == "n":
        
        print("Eliminación Cancelada, Fin del programa.")
        return
    
    try:
        send2trash(arch)
        
        print(f"El archivo {arch} enviado a la papelera.")
    
    except PermissionError:
    
        print(f"No tenés permisos para mover el archivo {arch} a la papelera.")
    
    except Exception as e:
    
        print(f"Error al mover el archivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        move_to_trash(file_path)
    else:
        print("Se te olvidó pasarme la ruta del archivo o el nombre.")
