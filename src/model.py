import tensorflow as tf
with tf.device('/CPU:0'):
    new_model = tf.keras.models.load_model('src\model.h5')

    def Predict_model(img):
        return new_model.predict(img)
