# AVOCADO

AVOCADO is an application that allows the user to upload any standard image, automatically generate a caption that describes the image, and automatically detect the number of faces in an image.

VIDEO DEMO: https://www.linkedin.com/feed/update/urn:li:activity:6733116808653488128/


## Project Description

a4 Advertising, is the cross-screen targeted advertising brand launched by Altice USA that has simplified the media planning process by introducing the next generation self-serving platform: Athena. With Athena, buyers and campaign managers are able to plan and activate cross-screen campaigns, locally  and nationally, within minutes. The idea for the project came out from a growing need to reliably capture useful metadata about the creatives that the advertising campaign managers and buyers upload to Athena. At one point, our team noticed that there was an unusual pattern of users uploading the wrong files, which had an effect on their delivery. Part of the reason why this happens is because Athena (as well as the DSPs that we partner with) treat political and commercial campaigns separately on the backend. If a user uploads political creatives for a commercial campaign, or vice versa, they may not be able to reach their expected target audiences. Although these errors are caught once the campaign launches and are usually corrected quickly, there are still costs that come with not reaching expected delivery in time.

Having the ability to scan creatives for metadata would not only help solve problems with human error, but would also add an additional layer of information about how our clients are using the platform. Data about campaign performance and audience segmentation are plentiful in our current state, but in-house creatives are not being analyzed on any mass scale. Information extracted from a creative could potentially enhance the our knowledge about our audience segments and how clients are using them. By combining campaign performance (i.e. daily impressions, pacing, CTR, etc.), one can eventually use this data to provide recommendations about which creatives tend to work best for their selected target audience.

To start the app, you will need to unzip the working prototype and click on avocadoBot.exe. This app was packaged on a Windows 10 PC with a 32-bit processor, so if you have a 64-bit or a different OS it may not work as intended. If you encounter any errors, please try using a different device, download the full app from github, or contact me for help. If the app runs correctly, you will be presented with a window displaying the app title, a default image of a firetruck, a welcome message, and three buttons for uploading new images, captioning them, and detecting any human faces. 

When you caption an image it may take a second or two to process it, so please be patient. The app will take the image displayed on screen, convert it to a tensor, and run it through a Encoder-Decoder neural network. The Encoder, a Convolution Neural Network (CNN), is responsible for taking the image tensor and return an "encoder vector" which would then be passed to the Decoder. The Decoder is an LSTM, a RNN-based network with long-short term memory. LSTMs are often used in natural language processing and time series data, but they can also create captions from image data which makes them a very good choice here. Once the image runs through the network, the final process would decode the output vector into readable text and output it to the screen. It's worth noting that anytime an image is uploaded to the app, a copy of that image is stored in `src\images` directory. There will be some example images that you can use in there, but copies of those images will still be created if you decide to use them. However, please do not modify or delete anything in the `src` directory. If there are any human faces displayed on the screen, you can click the third button to detect them.

One of the biggest learning challenges for me was hardware. The computer that I used to develop this app does not have a 64-bit processor or any GPUs. Initially I decided to use this computer because it had 32GB of RAM, which is the most memory that I have in any other computer in my possession. The hope was that I could build a small neural network and train it on CPU alone. However, I quickly realized that even with a single hidden layer of only 8 nodes, the training would take days to complete. To resolve this problem I trained the model externally in the Cloud using a GPU, and then copied the resulting model back into my application. However, training the model for five epochs still took about 15 hours to complete and it was the most that I could personally afford. Another challenge I had was building the interface with Tkinter because it was my first time doing it. I had to spend a few days last week going through online tutorials before I even got to training the neural network. Finally, being able to package the application and distribute was more difficult than I expected. This is the biggest project that I ever had to create an executable for, so I was not certain if it would work. After trying and failing to package it with pyinstaller library, I switched to using cx_freeze which required a bit more coding and troubleshooting. In the end, I was able to run the app successfully on my computer and I hope it runs well on yours!

`avocadoBot.exe` was developed entirely in Python using the following libraries:

```
click==7.1.2
cx-Freeze==6.3
dataclasses==0.6
future==0.18.2
importlib-metadata==2.0.0
joblib==0.17.0
nltk==3.5
numpy==1.19.4
opencv-python==4.4.0.46
pandas==1.1.4
Pillow==8.0.1
python-dateutil==2.8.1
pytz==2020.4
regex==2020.10.28
six==1.15.0
torch==1.7.0+cpu
torchaudio==0.7.0
torchvision==0.8.1+cpu
tqdm==4.51.0
typing-extensions==3.7.4.3
zipp==3.4.0
```



## Project Categories

Computer Vision, Natural Language Processing, & Machine Learning
