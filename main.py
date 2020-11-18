from flask import Flask, jsonify, request
from conexion  import crear_usuario

app = Flask(__name__)

#@app.route("/")
#def hola():
#    return "<h1>Hola Mundo!</h1>"

@app.route("/api/v1/usuarios", methods=["POST"])
def usuarios():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)

            if(crear_usuario(data['nombre'],data['apellidos'], data['contraseña'])):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "exist"})
        except:
            return jsonify({"code": "Error"})

app.run(debug=True)
