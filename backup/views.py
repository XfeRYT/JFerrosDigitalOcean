import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core import management
from datetime import datetime
from django.db import connection
import hashlib
import subprocess
import json
from django.db import IntegrityError

def restore_backup(request, filename):
    backup_dir = settings.BACKUP_ROOT
    backup_file_path = os.path.join(backup_dir, filename)

    if os.path.exists(backup_file_path):
        try:
            with connection.cursor() as cursor:
                # Opcionalmente, puedes deshabilitar las restricciones de clave externa aquí
                # cursor.execute('PRAGMA foreign_keys=off;')

                cursor.execute('BEGIN')
                with open(backup_file_path, 'r') as backup_file:
                    sql_statements = backup_file.read()
                    cursor.executescript(sql_statements)
                cursor.execute('COMMIT')

                # Opcionalmente, puedes volver a habilitar las restricciones de clave externa aquí
                # cursor.execute('PRAGMA foreign_keys=on;')

                return HttpResponse("Copia de seguridad restaurada exitosamente.")
        except IntegrityError as e:
            return HttpResponse(f"Error de integridad al restaurar la copia de seguridad: {str(e)}")
        except Exception as e:
            return HttpResponse(f"Error al restaurar la copia de seguridad: {str(e)}")
    else:
        return HttpResponse("La copia de seguridad seleccionada no existe.")



def list_backups(request):
    titulo= "Copias de Seguridad"
    backup_dir = settings.BACKUP_ROOT  # Directorio donde se almacenan las copias de seguridad
    backup_files = []

    for filename in os.listdir(backup_dir):
        if filename.endswith(".json"):
            backup_files.append(filename)

    context = {
        'backup_files': backup_files,
        'titulo' : titulo,
    }

    return render(request, 'backup/listar.html', context)


"""def backup_database(request):
    # Genera una copia de seguridad de la base de datos
    connection.close()
    backup_dir = settings.BACKUP_ROOT  # Directorio donde se guardarán las copias de seguridad

    # Obtén el contenido de la base de datos como una cadena
    management.call_command('dumpdata', '--output', 'current_backup.json')
    with open('current_backup.json', 'r') as current_backup_file:
        current_backup_content = current_backup_file.read()

    # Recorre las copias de seguridad existentes y compáralas
    for filename in os.listdir(backup_dir):
        if filename.endswith(".backup"):
            backup_file = os.path.join(backup_dir, filename)
            with open(backup_file, 'r') as existing_backup_file:
                existing_backup_content = existing_backup_file.read()

            # Calcula el hash de cada copia de seguridad
            current_hash = hashlib.md5(current_backup_content.encode()).hexdigest()
            existing_hash = hashlib.md5(existing_backup_content.encode()).hexdigest()

            if current_hash == existing_hash:
                os.remove('current_backup.json')  # Borra el archivo de copia de seguridad actual
                return HttpResponse("Ya existe una copia de seguridad idéntica.")

    # Si no se encontró una copia de seguridad idéntica, guarda la nueva copia
    backup_filename = f"CS_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.backup"
    backup_file_path = os.path.join(backup_dir, backup_filename)
    os.rename('current_backup.json', backup_file_path)
    return HttpResponse("Copia de seguridad creada correctamente.")"""

def backup_database(request):
    backup_dir = settings.BACKUP_ROOT  # Directorio donde se guardarán las copias de seguridad

    # Genera una copia de seguridad de la base de datos
    backup_filename = f"CS_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
    backup_file_path = os.path.join(backup_dir, backup_filename)

    try:
        management.call_command('dumpdata', '--output', backup_file_path)
        return HttpResponse("Copia de seguridad creada correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al crear la copia de seguridad: {str(e)}")