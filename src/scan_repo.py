import os 
import argparse
from pathlib import Path

def take_files(root_path_, target_extensions_, excluded_files_, excluded_dirs_):
    
    found_files = []
    
    # recorre los archivos y directorios de la ruta dada
    for dirpath, dirnames, filenames in os.walk(root_path_):

        # excluye directorios definidos
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs_]
        
        # excluye archivos definidos
        filenames[:] = [f for f in filenames if f not in excluded_files_ and Path(f).suffix.lower() in target_extensions_]

        # asigna los archivos seleccionados objetivo
        for file in filenames:
            found_files.append(
                Path(dirpath).resolve() / file
                )

    return found_files


def main():

    # input de directorio a analizar
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Ruta del directorio que se analizará")
    args = parser.parse_args()
    target_path = args.directory

    # definición de listas y diccionarios
    target_extensions = [".php", ".py", ".js", ".md"]
    excluded_dirs = [".git", ".venv", "node_modules", "vendor", ".pytest_cache"]
    excluded_files = [".gitignore", ".env"]
    counter = {}

    # flujo principal
    if target_path and Path(target_path).is_dir():
        target_files = take_files(target_path, target_extensions, excluded_files, excluded_dirs)
        for file in target_files:
            print(f"Archivo: {file}")
            print(f"Tamaño: {file.stat().st_size} bytes\n")
            ext = file.suffix.lower()
            counter[ext] = counter.get(ext, 0) + 1

        print(f"Total de archivos: {len(target_files)}")
        for extension,count in counter.items():
            print(f"{extension}: {count}")
    else:
        print(f"La ruta facilitada \"{target_path}\" no es correcta")


if __name__ == "__main__":
    main()