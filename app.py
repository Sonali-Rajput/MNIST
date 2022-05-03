import os
import cv2
from flask import Flask, request
from src.model import Predict_model
from src.image import image_BWresize
app = Flask(__name__)


@app.route("/api/v1/digit/", methods=['POST'])
def worker():
    if request.method == 'POST':
        recievedFile = request.files['file']
        recievedFile.save(recievedFile.filename)
        #img = cv2.imread(recievedFile.filename)
        image_data = image_BWresize(recievedFile.filename)
        os.remove(recievedFile.filename)
        prediction = Predict_model(image_data)
        # print(prediction)
        return str(prediction)


if __name__ == "__main__":
    app.run(debug=True)
