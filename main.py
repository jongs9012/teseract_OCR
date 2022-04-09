from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
images = ["test_1.jpg", "test_2.gif", "test_3.jpg", "test_4.jpg", "test_5.jpg", "test_6.jpg", "Ukraine.png"]

for index in range(0, len(images)):
    filename = f"images/{images[index]}"
    image = Image.open(filename)
    text = image_to_string(image, lang="kor")

    with open(f"results/{images[index][0:-4]}.txt", "w") as f:
        f.write(text)
