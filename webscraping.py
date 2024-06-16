from bs4 import BeautifulSoup
import requests
import time
import webbrowser


url = requests.get("https://listado.mercadolibre.com.ec/celulares#D")

soup = BeautifulSoup(url.content, "html.parser")
entrada = soup.find_all("div", {"class": "ui-search-result__content-wrapper"})
#Producto encontrado en la web se va a almacenar en productos
productos = []

for producto in entrada:
#Encontramos nombre y precio del producto
    nombre = producto.find('h2', class_='ui-search-item__title')
    precio = producto.find('span', class_='andes-money-amount__fraction')
    if nombre and precio:
#Tomamos nombre y precio del producto únicamente
        nombreActual_text = nombre.text.strip()
        precioActual_text = precio.text.strip()
#Impresión del nombre y el precio del producto
        print(f"Nombre: {nombreActual_text}")
        print(f"Precio: {precioActual_text} $")
#Divido producto con * 
        print("*"*8)
#Guardamos información del producto nombre y precio en un diccionario
    product_info = {
        "Nombre": nombreActual_text,
        "Precio": precioActual_text + "$"
    }
#Se agrega el diccionario a la lista productos
    productos.append(product_info)