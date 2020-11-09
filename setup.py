from cx_Freeze import setup, Executable

# import checks
import tkinter
import PIL
import pandas
import torchvision
import numpy
import torch
import nltk
import cv2

startup_file = "avocadoBot.py"
icon = "icon.ico"
base = "Win32GUI"

include_files = ["src/"]

packages = ["cx_Freeze", "tkinter", "PIL", "pandas", "torchvision", "numpy", "torch", "nltk", "cv2"]

exe = Executable(script=startup_file, base=base, icon=icon)

options = {"build_exe": {
    "build_exe" : ".//build",
    "packages": packages,
    "include_files": include_files
    }
}

setup(
    name = "avocadoBot",
    version = "1",
    description = "a4 advertising photo caption & face detection bot",
    author = "Akim Adams",
    author_email = "akim.adams@a4media.com",
    options = options,
    executables = [exe]
)

