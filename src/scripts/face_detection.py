import cv2
from PIL import Image, ImageTk

def load_image_for_face_detection(img_path):
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def load_face_detection_model(model_path):
    model = cv2.CascadeClassifier(model_path)
    return model

def detect_faces(image, model, scaleFactor=1.25, minNeighbors=5):
    faces = model.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    try:
        num_faces_found = faces.shape[0]
        image_with_detections = image.copy()
        for (x,y,w,h) in faces:
            cv2.rectangle(image_with_detections,(x,y),(x+w,y+h),(255,0,0),3)
    except AttributeError as e:
        print("No faces found")
        image_with_detections = None
        num_faces_found = 0

    return image_with_detections, num_faces_found

def run(image_name):
    img_path = f"./src/images/{image_name}"
    model_path = './src/models/haarcascade_frontalface_default.xml'
    image_to_detect = load_image_for_face_detection(img_path)
    model = load_face_detection_model(model_path)
    image_with_detections, num_faces_found = detect_faces(image_to_detect, model)
    if num_faces_found > 0:
        image = Image.fromarray(image_with_detections)
        scale_w = 500 / image.width
        scale_h = 400 / image.height
        w = int(image.width * scale_w)
        h = int(image.height * scale_h)
        image = image.resize((w, h), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image=image)
    else:
        photo = None
        num_faces_found = 0

    return photo, num_faces_found
