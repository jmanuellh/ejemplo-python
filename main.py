from flask import Flask
import requests

# Hacer una petición a la API de JSONPlaceholder para obtener todos los posts
# response = requests.get('https://jsonplaceholder.typicode.com/posts')

app = Flask(__name__)

@app.route('/')
def hello():
    # # Verificar si la petición fue exitosa (código de estado 200)
    # if response.status_code == 200:
    #     # Convertir la respuesta JSON a un objeto Python
    #     posts = response.json()

    #     # Obtener el título del primer post
    #     first_post_title = posts[0]['title']

    #     return first_post_title
    # else:
    #     return f"Error al obtener los posts: {response.status_code}"
    return 'hola'

if __name__ == '__main__':
    app.run(debug=True)






