from flask import Flask , request
from src.model import Predict_model
from src.image import image_BWresize
app = Flask(__name__)

@app.route("/api/v1/digit/",methods=['POST','GET'])
def worker():
    data = request.get_data()
    image_data = image_BWresize(data)
    prediction = Predict_model(image_data)
    return str(prediction)

if __name__ == "__main__":
    app.run(debug=True)
