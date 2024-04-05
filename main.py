from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
from googletrans import Translator
import os
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_image = 'samsarandsp.png'
pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)
translator = Translator(service_urls=['translate.google.com'])
translated_text = translator.translate(text, dest='ta').text
print(translated_text)
language = 'ta'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("output.mp3")
os.system("start output.mp3")
