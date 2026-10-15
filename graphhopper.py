import requests
import urllib.parse

API_KEY = "b75b825c-aec5-48e8-bd61-d98b4cb344c1"

def obtener_coordenadas(lugar):
    url = "https://graphhopper.com/api/1/geocode/"
    parametros = {
        "q": lugar,
        "locale": "es",
        "key": API_KEY,
        "limit": 1
    }

    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()

    if respuesta.status_code == 200 and datos.get("hits"):
        punto = datos["hits"][0]["point"]
        return f'{punto["lat"]},{punto["lng"]}'

    return None


while True:
    origen = input("Ingrese el lugar de origen (o 's' para salir): ")

    if origen.lower() in ["s", "salir"]:
        print("Saliendo del programa.")
        break

    destino = input("Ingrese el lugar de destino (o 's' para salir): ")

    if destino.lower() in ["s", "salir"]:
        print("Saliendo del programa.")
        break

    coordenadas_origen = obtener_coordenadas(origen)
    coordenadas_destino = obtener_coordenadas(destino)

    if not coordenadas_origen or not coordenadas_destino:
        print("No se pudo encontrar el origen o el destino. Intente nuevamente.\n")
        continue

    url = "https://graphhopper.com/api/1/route"

    parametros = {
        "key": API_KEY,
        "point": [coordenadas_origen, coordenadas_destino],
        "vehicle": "car",
        "locale": "es",
        "instructions": "true"
    }

    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        ruta = datos["paths"][0]

        distancia = ruta["distance"] / 1000
        tiempo = ruta["time"] / 60000

        print(f"\nDistancia: {distancia:.2f} km")
        print(f"Tiempo estimado: {tiempo:.2f} minutos")
        print("\nInstrucciones del viaje:")

        for instruccion in ruta["instructions"]:
            print(instruccion["text"])

    else:
        print("Error al obtener la ruta.")
        print(datos.get("message", "Error desconocido."))

    print()