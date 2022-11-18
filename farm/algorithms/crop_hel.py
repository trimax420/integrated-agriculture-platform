import os
import cv2
import numpy as np
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf
from tensorflow.keras.preprocessing.image  import load_img , img_to_array 
from keras.models import  load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
os.environ['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'
print(os.getenv('TF_GPU_ALLOCATOR'))
# load model

def main():
    model = load_model("/home/trimax/Desktop/integrated-agriculture-platform/farm/datasets/leaf_model.h5")


    face_haar_cascade = cv2.CascadeClassifier('/home/trimax/Desktop/integrated-agriculture-platform/farm/datasets/cascade.xml')


    cap = cv2.VideoCapture(0)

    while True:
        ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
        if not ret:
            continue
        gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

        faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
            roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
            roi_gray = cv2.resize(roi_gray, (224, 224))
            img_pixels = img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255

            predictions = model.predict(img_pixels)

            # find max indexed array
            max_index = np.argmax(predictions[0])

            crop= ('Apple Scab Leaf','Apple leaf','Apple rust leaf',
                'Bell_pepper leaf','Bell_pepper leaf spot','Blueberry leaf',
                    'Cherry leaf','Corn Gray leaf spot','Corn leaf blight',
                    'Corn rust leaf','Peach leaf','Potato leaf early blight',
                    'Potato leaf late blight','Raspberry leaf','Soyabean leaf',
                    'Squash Powdery mildew leaf','Strawberry leaf','Tomato Early blight leaf',
                    'Tomato Septoria leaf spot','Tomato leaf','Tomato leaf bacterial spot',
                    'Tomato leaf late blight','Tomato leaf mosaic virus','Tomato leaf yellow virus',
                    'Tomato mold leaf','grape leaf','grape leaf black rot')
            predicted_emotion = crop[max_index]

            cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('Facial emotion analysis ', resized_img)

        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows