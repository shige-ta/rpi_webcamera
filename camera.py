from datetime import datetime
import cv2, os
from flask import Flask, jsonify, request
import base64
import time

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
  current_dir = os.path.dirname(os.path.abspath(__file__)) + '/'

  cam = cv2.VideoCapture(0)

  if cam == None:
    return False

  _, img = cam.read()


  shoot_time = datetime.now()
  image_file = current_dir + shoot_time.strftime('%Y%m%d_%H%M%S%f') +'.jpg'

  cv2.imwrite(image_file, img)
  cam.release()
  cv2.destroyAllWindows()
  print("camera")

  with open(image_file, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode('utf-8')

  return img_base64

if __name__ == "__main__":
  app.run(host='0.0.0.0')
