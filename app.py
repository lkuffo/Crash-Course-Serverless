from flask import Flask


app = Flask('app')

productos = {
    1: "Hello Kitty",
    2: "Peluche",
    3: "Carrito"
}


@app.route("/productos", methods=["GET"])
def get_productos():
    return productos, 200


@app.route("/productos/<id>", methods=["DELETE"])
def delete_productos(id):
    del productos[id]
    return productos, 200
