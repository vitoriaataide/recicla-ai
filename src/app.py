from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = tf.keras.models.load_model("modelo_reciclagem.h5")

classes = {
    0: "Papel/Papelão",
    1: "Vidro",
    2: "Metal",
    3: "Plástico"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    confianca = None

    if request.method == "POST":
        arquivo = request.files["imagem"]

        if arquivo:
            caminho = os.path.join("static", arquivo.filename)
            arquivo.save(caminho)

            img = image.load_img(caminho, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            previsao = model.predict(img_array)
            indice = np.argmax(previsao)
            confianca = float(np.max(previsao) * 100)

            resultado = classes[indice]

    return render_template(
        "index.html",
        resultado=resultado,
        confianca=confianca
    )

if __name__ == "__main__":
    app.run(debug=True)