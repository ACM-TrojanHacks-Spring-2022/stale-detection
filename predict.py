
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import tensorflow as tf 
f = open("model.json","r")
loaded_model_json = f.read()
f.close()

model =  tf.keras.models.model_from_json(loaded_model_json)
model.load_weights('model.h5')

location = "test.jpg"
img = load_img(location,target_size=(224,224,3))
from tensorflow.keras.preprocessing.image import img_to_array
img = img_to_array(img)
img = img/255

img = np.expand_dims(img,[0])
answer = model.predict(img)

print(answer)