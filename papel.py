import sys
import os
from send2trash import send2trash

def move_to_trash(file_path):
    try:
        # Normaliza y convierte la ruta a absoluta
        arch = os.path.abspath(file_path)
        print(f"Intentando mover el archivo: {arch} a la papelera.")
        
        print(f"Seguro que querés mandar {arch} a la papelera? S(sí), N(No)")
        rta = input().lower()
        
        if rta == "n":
            print("Eliminación Cancelada, Fin del programa.")
            return
        
        send2trash(arch)
        print(f"El archivo {arch} enviado a la papelera.")
    except PermissionError:
        print(f"No tenés permisos para mover el archivo {arch} a la papelera.")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

def handle_error(e):
    """Manejo de excepciones para capturar errores de ejecución."""
    if isinstance(e, TypeError):
        print("Error: No se pasó el archivo correctamente. Asegúrate de incluir el nombre o la ruta del archivo.")
    else:
        print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            # Si no se pasa una ruta completa, buscar el archivo en el directorio actual
            file_path = sys.argv[1]
            if not os.path.isabs(file_path):  # Si el archivo no tiene ruta completa
                file_path = os.path.join(os.getcwd(), file_path)  # Agregar el directorio actual
            
            if os.path.exists(file_path):  # Verificar si el archivo existe
                move_to_trash(file_path)
            else:
                print(f"El archivo {file_path} no existe.")
        else:
            print("Se te olvidó pasarme la ruta del archivo o el nombre.")
    except Exception as e:
        handle_error(e)
