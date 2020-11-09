import tkinter as tk
from tkinter import ttk
from src.scripts.orchestrator import *
from PIL import Image, ImageTk


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        # INITIALIZE
        super().__init__(parent)
        self.controller = controller
        self.job_running = False
        self.image_name = "avocadoBot_0.png"     # default startup image

        # HEADER LABEL
        self.header_label = tk.StringVar(value="a4 advertising photo caption & face detection bot")

        label = ttk.Label(
            self,
            textvariable=self.header_label,
            font=("Courier", 12, 'bold')
        )
        label.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(20, 10))

        # MAIN FRAME
        main_frame = ttk.Frame(self, height="400", width="600")
        main_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")
        image = Image.open(f"./src/misc/{self.image_name}")
        scale_w = 500 / image.width
        scale_h = 400 / image.height
        w = int(image.width * scale_w)
        h = int(image.height * scale_h)
        image = image.resize((w, h), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.image_label = ttk.Label(main_frame, image=photo, compound="top")
        self.image_label.image = photo
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")
        self.caption_label = ttk.Label(self,
                                      text="Welcome! Press the buttons below to caption this photo, or upload your own image!",
                                      font=("Courier", 9, 'bold'))
        self.caption_label.grid(row=2, column=0, sticky="W", padx=(10, 0), pady=(10, 30))

        # BUTTON CONTROLS
        button_container = ttk.Frame(self, padding=10)
        button_container.grid(row=3, column=0, columnspan=2, sticky="EW")
        button_container.columnconfigure((0, 1, 2), weight=1)

        self.load_button = ttk.Button(
            button_container,
            text="Upload Image",
            command=self.exec_load_image,
            cursor="hand2"
        )
        self.load_button.grid(row=0, column=0, sticky="EW")

        self.caption_button = ttk.Button(
            button_container,
            text="Caption Me!",
            command=self.exec_caption_image,
            cursor="hand2"
        )
        self.caption_button.grid(row=0, column=1, sticky="EW", padx=5)

        self.face_detect_button = ttk.Button(
            button_container,
            text="Find Faces",
            command=self.exec_detect_faces,
            cursor="hand2"
        )
        self.face_detect_button.grid(row=0, column=2, sticky="EW")


    def exec_load_image(self):
        try:
            new_image_path = O_get_new_image_path()
            photo = O_load_photo(new_image_path)
            self.image_name = new_image_path.split("/")[-1]
            self.image_label['image'] = photo
            self.image_label.image = photo
            self.image_label['text'] = ""
            self.caption_label['text'] = "Press the buttons below to caption this photo, or upload your own image!"
        except Exception as e:
            print("Internal error, can't load image :(", e)

    def exec_caption_image(self):
        if self.image_name != "avocadoBot_0.png":
            try:
                new_caption = O_caption_image(self.image_name)
                self.caption_label['text'] = new_caption
            except Exception as e:
                print("Internal error, can't caption image :(", e)
                self.caption_label['text'] = "not sure what this is . please upload another image ."
        else:
            self.caption_label['text'] = "hi, i'm avocadoBot . please upload another image ."


    def exec_detect_faces(self):
        if self.image_name != "avocadoBot_0.png":
            try:
                photo, num_faces = O_detect_faces(self.image_name)
                if photo != None:
                    self.image_label['image'] = photo
                    self.image_label.image = photo
                    self.caption_label['text'] = f"Total faces found: {num_faces}"
                else:
                    self.caption_label['text'] = "could not find any faces . please upload another image ."
            except Exception as e:
                print("Internal error, can't caption image :(", e)
                self.caption_label['text'] = "could not find any faces . please upload another image ."
        else:
            self.caption_label['text'] = "that's not a face, i'm avocadoBot . please upload another image ."