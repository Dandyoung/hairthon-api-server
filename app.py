from flask import Flask, request
from flask_cors import CORS
import keras
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

#정현님이 말씀하신 에러때문에 넣은 코드..
app = Flask(__name__)
CORS(app)

def ajaxImage(imageSize):
    content = request.values['image'].split(';')[1]
    image_encoded = content.split(',')[1]
    body = base64.decodebytes(image_encoded.encode('utf-8'))
    img = np.array(Image.open(BytesIO(body)).convert("L"))
    image = cv2.resize(img, imageSize)/255.0
    image = np.reshape(image, (1, imageSize[0], imageSize[1]))
    return image

@app.route('/predict', methods=['GET'])
def ajax():
    image = ajaxImage((28,28))
    model = keras.models.load_model("converted_model.h5")
    prediction = model.predict(image)[0]
    return {'answer': int(np.argmax(prediction))}
    

#0.0.0.0은 외부에서의 접근을 허용한다는 뜻이고, 우리가 제공받은 포트는 5000번입니다~
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=False)