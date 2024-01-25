from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo para los artículos del blog
entradas = [
    {
        'titulo': 'El Clásico: Real Madrid vs Barcelona',
        'contenido': 'Un emocionante partido entre dos de los equipos más grandes de España.',
        'autor': 'John Doe',
    },
    {
        'titulo': 'Champions League: Resumen de la temporada',
        'contenido': 'Los mejores momentos de la última temporada de la Liga de Campeones.',
        'autor': 'Jane Smith',
    },
    # Agrega más entradas según sea necesario
]

@app.route('/')
def inicio():
    return render_template('index.html', entradas=entradas)

if __name__ == '__main__':
    app.run(debug=True)
