import requests

# Hacer una petición a la API de JSONPlaceholder para obtener todos los posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Verificar si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta JSON a un objeto Python
    posts = response.json()

    # Obtener el título del primer post
    first_post_title = posts[0]['title']

    print(first_post_title)
else:
    print(f"Error al obtener los posts: {response.status_code}")