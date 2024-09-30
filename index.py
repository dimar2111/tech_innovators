from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    """Renderiza la página de inicio."""
    return render_template('home.html')

@app.route('/contenido')
def contenido():
    """Renderiza la página de contenido."""
    return render_template('contenido.html')

@app.route('/about')
def about():
    """Renderiza la página de información."""
    return render_template('about.html')

if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración
    app.run(debug=True)

