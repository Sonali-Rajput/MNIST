import tensorflow as tf
new_model = tf.keras.models.load_model('src\model.h5')
def Predict_model(img):
    return new_model.predict(img)
