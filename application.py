# Victor Manuel Alonso Miranda

# Importamos las librerías
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS, cross_origin

# Ahora conectamos con la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="apivictor"
)

# Creamos la app del server
app = Flask(__name__)

# Configuramos el CORS (Cross-Origin Resource Sharing)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# Añadimos una ruta de prueba
@app.route('/hello')
def hello_world():
    return 'Hola, mundo!'

# Método GET: para obtener todas las películas
@app.route('/peliculas/', methods=['GET'])
def obtener_peliculas():
    mycursor = mydb.cursor()
    # Añadimos la consulta SQL para obtener todas las películas
    mycursor.execute("SELECT * FROM peliculas")
    resultados = mycursor.fetchall()
    # Creamos una lista vacía para almacenarlas
    peliculas = []
    # Ahora creamos un diccionario con la información de cada película
    for resultado in resultados:
        pelicula = {
            "id": resultado[0],
            "nombre": resultado[1],
            "año": resultado[2],
            "director": resultado[3],
            "genero": resultado[4]
        }
        # La agregamos a la lista "pelicula"
        peliculas.append(pelicula)
    # Y ahora retornamos la lista de películas en formato JSON
    return jsonify({"peliculas":peliculas})

# Método GET: para obtener una película por su ID
@app.route('/peliculas/<int:id>', methods=['GET'])
def obtener_pelicula(id):
    mycursor = mydb.cursor()
    # Ejecutamos la consulta SQL para sacar la película con una ID específica
    mycursor.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
    resultado = mycursor.fetchone()
    # En el caso de encontrar la película, creamos un diccionario y lo pasamos a JSON
    if resultado:
        pelicula = {
            "id": resultado[0],
            "nombre": resultado[1],
            "año": resultado[2],
            "director": resultado[3],
            "genero": resultado[4]
        }
        return jsonify(pelicula)
    # En el caso de no encontrarla, enviamos un mensaje de error con un código de estado 404
    else:
        return jsonify({"mensaje": "Pelicula no encontrada"}), 404

# Método POST: para agregar una película nueva a la base de datos
@app.route('/peliculasPost/', methods=['POST'])
def agregar_pelicula():
    # Añadimos los datos en formato JSON
    nueva_pelicula = {
        "nombre": request.json['nombre'],
        "año" : request.json['año'],
        "director": request.json['director'],
        "genero": request.json['genero']
    }
    mycursor = mydb.cursor()
    # Ejecutamos la consulta SQL que nos permite añadirlo a la base de datos
    sql = "INSERT INTO peliculas (nombre, año, director, genero) VALUES (%s, %s, %s, %s)"
    val = (nueva_pelicula['nombre'], nueva_pelicula['año'], nueva_pelicula['director'], nueva_pelicula['genero'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    return nueva_pelicula

# Método POST: para agregar una película nueva a la base de datos pero por el enlace
@app.route('/peliculasPost/<int:id>/<nombre>/<int:anio>/<director>/<genero>', methods=['POST'])
def agregar_pelicula_url(id, nombre, anio, director, genero):
    mycursor = mydb.cursor()
    # Ejecutamos la consulta SQL que nos permite añadirlo a la base de datos
    sql = "INSERT INTO peliculas (id, nombre, año, director, genero) VALUES (%s, %s, %s, %s, %s)"
    val = (id, nombre, anio, director, genero)
    mycursor.execute(sql, val)
    mydb.commit()
    return jsonify({"mensaje": "Pelicula agregada correctamente"})

# Método PUT: modificar cualquier dato de una película
@app.route('/pelicula/<int:id>', methods=['PUT'])
def editar_pelicula(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
    peliculaEncontrada = mycursor.fetchone()
    if peliculaEncontrada is None:
        return jsonify({'mensaje': 'Pelicula no encontrada'}), 404
    
    pelicula_data = request.get_json()
    nueva_pelicula = {
        'id': id,
        'nombre': pelicula_data.get('nombre', peliculaEncontrada[1]),
        'año': pelicula_data.get('año', peliculaEncontrada[2]),
        'director': pelicula_data.get('director', peliculaEncontrada[3]),
        'genero': pelicula_data.get('genero', peliculaEncontrada[4])
    }

    query = "UPDATE peliculas SET nombre = %s, año = %s, director = %s, genero = %s WHERE id = %s"
    values = (nueva_pelicula['nombre'], nueva_pelicula['año'], nueva_pelicula['director'], nueva_pelicula['genero'], id)
    mycursor.execute(query, values)
    mydb.commit()

    return jsonify(nueva_pelicula)


# Método PUT: editar el genero de una película por su id en una app como Insomnia o Postman
@app.route('/peliculasgenero/<int:id>', methods=['PUT'])   
def editar_genero_pelicula_app(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
    peliculaEncontrada = mycursor.fetchone()
    
    if peliculaEncontrada is None:
        return jsonify({'mensaje': 'Pelicula no encontrada'}), 404
    
    nuevo_genero = request.json.get('genero')

    query = "UPDATE peliculas SET genero = %s WHERE id = %s"
    values = (nuevo_genero, id)
    mycursor.execute(query, values)
    mydb.commit()

    mycursor.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
    peliculaActualizada = mycursor.fetchone()
    return jsonify(peliculaActualizada)


# Método PUT: modificar el genero de una película por su id a través de la URL
@app.route('/peliculas/<int:id>/genero', methods=['PUT'])
def editar_genero_pelicula_url(id):
    nuevo_genero = request.args.get('nuevo_genero')
    mycursor = mydb.cursor()
    query = "UPDATE peliculas SET genero = %s WHERE id = %s"
    values = (nuevo_genero, id)
    mycursor.execute(query, values)
    mydb.commit()

    return jsonify({'mensaje': f'genero de la pelicula con ID {id} actualizado correctamente a "{nuevo_genero}"'})
    

# Método DELETE: eliminar una película por su ID
@app.route('/peliculasDelete/<int:id>', methods=['DELETE'])
def eliminar_pelicula(id):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM peliculas WHERE id = %s", (id,))
    mydb.commit()

    return jsonify({"mensaje": "Pelicula eliminada correctamente"})