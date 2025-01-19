import os

extract_path = 'ruta/a/tu/directorio'
main_dir = os.path.join(extract_path, 'ProjectCV2P-main')

# Resto de tu código


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido! Esta es la página principal de tu proyecto."

if __name__ == "__main__":
    app.run(debug=True)
