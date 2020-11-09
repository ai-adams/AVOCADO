def O_get_new_image_path():
    from src.scripts.load_image import get_new_image_path
    new_image_path = get_new_image_path()
    return new_image_path

def O_load_photo(path):
    from src.scripts.load_image import get_photo
    photo = get_photo(path)
    return photo

def O_caption_image(image_name):
    from src.scripts.caption_image import run
    caption = run(image_name)
    return caption

def O_detect_faces(image_name):
    from src.scripts.face_detection import run
    photo, num_faces = run(image_name)
    return photo, num_faces