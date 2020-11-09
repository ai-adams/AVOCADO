from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import getpass


def save_image(old_path, new_path):
    saved = False
    try:
        image = Image.open(old_path)
        image.save(new_path)
        saved = True
    except AttributeError as e:
        print("CAN'T SAVE FILE", e)
        pass
    return saved


def get_new_image_path():
    usr = getpass.getuser()
    path = filedialog.askopenfilename(initialdir=f"./", title="Select file",
                                      filetypes=(("All files", "*.*"), ("PNG files", "*.png")))
    df_info = pd.read_csv("./src/misc/image_info.csv")
    assigned_id = int(df_info.iloc[-1]["IMG_ID"]) + 1
    filename = path.split("/")[-1]
    new_name = filename.split(".")[0] + f"_{assigned_id}"
    file_type = filename.split(".")[-1]
    image_name = f"{new_name}.{file_type}"
    new_path = f"./src/images/{image_name}"
    saved = save_image(path, new_path)
    if saved == True:
        dfx = pd.DataFrame({"IMG_ID": [assigned_id], "NAME": [new_name], "FILE_TYPE": [f".{file_type}"]})
        df = pd.concat([df_info, dfx])
        df.to_csv("./src/misc/image_info.csv", index=False)
    else:
        new_path = "./src/misc/avocadoBot_0.png"

    return new_path


def get_photo(path):
    try:
        image = Image.open(path)
        scale_w = 500 / image.width
        scale_h = 400 / image.height
        w = int(image.width * scale_w)
        h = int(image.height * scale_h)
        image = image.resize((w,h), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
    except AttributeError as e:
        image = Image.open(f"./src/misc/avocadoBot_0.png")
        scale_w = 500 / image.width
        scale_h = 400 / image.height
        w = int(image.width * scale_w)
        h = int(image.height * scale_h)
        image = image.resize((w, h), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

    return photo