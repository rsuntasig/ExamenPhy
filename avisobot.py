import requests
from webscraping import producto
from webscraping import productos


#Token y ID del bot que se crea
token_bot = "6768576443:AAFMp-wAJYttzJWJ8uoolze3BVsS8CuSo7Q"
chat_id = "1642125106"
def enviar_mensaje_telegram(producto):
    nombre = producto["Nombre"]
    precio = producto["Precio"]
    mensaje = f"**Producto:** {nombre}\n**Precio:** {precio}\n **Link:https://listado.mercadolibre.com.ec/celulares#D "

    url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
  
    data = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "Markdown"  
    }

    response = requests.post(url, json=data)
    #verificamos el status 200 es igual a que la solicitud se ejecutó correctamente
    if response.status_code != 200:
        print(f"Error al intentar enviar mensaje: {response.status_code}")

for producto in productos:
    enviar_mensaje_telegram(producto)