import json
import os
import time

DATA_FILE = "pymusic_data.json"

# Cargar datos desde archivo JSON o iniciar estructura vacía
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"catalogo": [], "playlists": {}, "usuarios": {}}

# Guardar datos en archivo JSON
def guardar_datos(datos):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)

#  Agregar una canción al catálogo
def agregar_cancion(catalogo, generos_set):
    print("🔧 Aquí se agregaría una nueva canción al catálogo.")
    # TODO: Pedir título, artista, género, duración
    # TODO: Crear un diccionario que contenga además de los datos anteriores:
    #       likes: 0, dislikes: 0, reproducciones: 0
    # TODO: Agregar canción al catálogo
    # TODO: Agregar el género al set generos_set
#comentario
#  Buscar canciones por título o artista
def buscar_cancion(catalogo):
    print("🔧 Aquí se buscarían canciones por título o artista.")
    # TODO: Pedir texto de búsqueda e imprimir coincidencias

#  Filtrar canciones por género
def filtrar_genero(catalogo, generos_set):
    print("🔧 Aquí se filtraría el catálogo por género musical.")
    # TODO: Mostrar todos los géneros únicos y pedir uno
    # TODO: Mostrar solo las canciones que tengan ese género

#  Crear una nueva playlist
def crear_playlist(playlists, catalogo):
    print("🔧 Aquí se crearía una nueva playlist.")
    # TODO: Pedir nombre de la playlist
    # TODO: Permitir agregar canciones por su título o ID
    # TODO: Validar que existan y agregarlas a la playlist

#  Reproducir canción (simular reproducción)
def reproducir_cancion(catalogo, historial):
    print("🔧 Aquí se simularía la reproducción de una canción.")
    # TODO: Pedir título de canción
    # TODO: Simular la reproducción con time.sleep(2)
    # TODO: Sumar +1 a 'reproducciones' y agregar al historial del usuario

#  Ver el top 3 de canciones más reproducidas
def ver_top_3(catalogo):
    print("🔧 Aquí se mostrarían las canciones más escuchadas.")
    # TODO: Ordenar por 'reproducciones' y mostrar las 3 más altas

#  Dar like/dislike a una canción
def reaccionar_cancion(catalogo):
    print("🔧 Aquí se agregaría un like o dislike a una canción.")
    # TODO: Pedir título de la canción
    # TODO: Preguntar si es like o dislike y sumar +1 al campo correspondiente

#  Editar una canción del catálogo
def editar_cancion(catalogo):
    print("🔧 Aquí se editaría la información de una canción.")
    # TODO: Buscar canción por título
    # TODO: Mostrar sus datos actuales
    # TODO: Pedir al usuario los nuevos datos (o mantener los actuales)
    # TODO: Actualizar el diccionario de esa canción

#  Eliminar una canción del catálogo
def eliminar_cancion(catalogo):
    print("🔧 Aquí se eliminaría una canción del catálogo.")
    # TODO: Pedir título de canción
    # TODO: Confirmar y eliminar de la lista

#  Iniciar sesión como usuario
def iniciar_sesion(usuarios):
    print("🔐 Iniciar sesión de usuario.")
    # TODO: Pedir nombre de usuario
    # TODO: Si no existe, crearlo con campos 'historial' y 'playlists'
    # TODO: Retornar el nombre de usuario actual

#  Mostrar historial del usuario
def mostrar_historial(historial, catalogo):
    print("🧾 Historial de canciones reproducidas.")
    # TODO: Recorrer lista de títulos y mostrar detalles de cada canción

# Menú principal
def menu():
    datos = cargar_datos()
    catalogo = datos["catalogo"]
    playlists = datos["playlists"]
    usuarios = datos["usuarios"]
    generos_set = set([c["genero"] for c in catalogo])

    # Iniciar sesión del usuario
    usuario = iniciar_sesion(usuarios)
    historial = usuarios[usuario]["historial"]
    user_playlists = usuarios[usuario]["playlists"]

    while True:
        print("\n🎼 PyMusic – Proyecto Final en Consola 🎵")
        print("1. Agregar canción")
        print("2. Buscar canción")
        print("3. Filtrar por género")
        print("4. Crear playlist")
        print("5. Reproducir canción")
        print("6. Ver top 3 canciones más escuchadas")
        print("7. Like / Dislike canción")
        print("8. Editar canción")
        print("9. Eliminar canción")
        print("10. Ver historial")
        print("11. Guardar y salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cancion(catalogo, generos_set)
        elif opcion == "2":
            buscar_cancion(catalogo)
        elif opcion == "3":
            filtrar_genero(catalogo, generos_set)
        elif opcion == "4":
            crear_playlist(user_playlists, catalogo)
        elif opcion == "5":
            reproducir_cancion(catalogo, historial)
        elif opcion == "6":
            ver_top_3(catalogo)
        elif opcion == "7":
            reaccionar_cancion(catalogo)
        elif opcion == "8":
            editar_cancion(catalogo)
        elif opcion == "9":
            eliminar_cancion(catalogo)
        elif opcion == "10":
            mostrar_historial(historial, catalogo)
        elif opcion == "11":
            guardar_datos({
                "catalogo": catalogo,
                "playlists": playlists,
                "usuarios": usuarios
            })
            print("💾 Cambios guardados. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar el programa
menu()
