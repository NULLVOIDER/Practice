import os
import Tesseract
import gTTS

print(Tesseract.image_to_string(image.open()))
lang = "english"
spell = gTTS(lang=english, text=mytext, slow=True)
os.save("welcome.mp3")
os.system("mpg321 welcome.mp3")